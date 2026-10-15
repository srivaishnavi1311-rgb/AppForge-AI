(() => {
  const state = {
    tasks: [],
    subjects: [],
    currentScreen: 'dashboard',
    editingTaskId: null,
  };

  // Mock data
  function initMock() {
    state.subjects = [
      { id: 'sub1', name: 'Math', color: '#ff5722' },
      { id: 'sub2', name: 'History', color: '#9c27b0' },
      { id: 'sub3', name: 'Physics', color: '#03a9f4' },
    ];
    const today = new Date().toISOString().split('T')[0];
    state.tasks = [
      { id: 't1', title: 'Read chapter 4', due: today, subject: 'sub1', status: 'pending' },
      { id: 't2', title: 'Essay draft', due: today, subject: 'sub2', status: 'pending' },
      { id: 't3', title: 'Lab report', due: new Date(Date.now()+86400000).toISOString().split('T')[0], subject: 'sub3', status: 'pending' },
    ];
  }

  // Helpers
  const $ = (s) => document.querySelector(s);
  const $$ = (s) => Array.from(document.querySelectorAll(s));

  function showToast(msg) {
    const toast = $('#toast');
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 3000);
  }

  // Rendering
  function renderScreen() {
    const container = $('#mainContent');
    container.innerHTML = '';
    if (state.currentScreen === 'dashboard') renderDashboard();
    else if (state.currentScreen === 'tasks') renderTasks();
    else if (state.currentScreen === 'subjects') renderSubjects();
    $('#pageTitle').textContent = capitalize(state.currentScreen);
    setActiveNav();
  }

  function renderDashboard() {
    const container = $('#mainContent');
    const today = new Date().toISOString().split('T')[0];
    const todayTasks = state.tasks.filter(t => t.due === today && t.status !== 'completed');
    const upcoming = state.tasks.filter(t => new Date(t.due) > new Date() && t.status !== 'completed');
    const completedCount = state.tasks.filter(t => t.status === 'completed').length;
    const total = state.tasks.length;
    const progress = total ? Math.round((completedCount/total)*100) : 0;

    const html = `
      <section class="grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));">
        <div class="card stat-card"><h2>Today's Tasks</h2><h3>${todayTasks.length}</h3></div>
        <div class="card stat-card"><h2>Upcoming</h2><h3>${upcoming.length}</h3></div>
        <div class="card stat-card"><h2>Progress</h2><h3>${progress}%</h3></div>
      </section>
      <section class="card" style="margin-top:1rem;">
        <h2>Today's Priorities</h2>
        <ul>
          ${todayTasks.map(t => `<li><a href="#" class="task-link" data-id="${t.id}">${t.title}</a> <span class="badge ${t.status}">${t.status}</span></li>`).join('')}
        </ul>
      </section>
    `;
    container.innerHTML = html;
    $$('.task-link').forEach(el => el.addEventListener('click', e => { e.preventDefault(); openTaskDetail(e.target.dataset.id); }));
  }

  function renderTasks() {
    const container = $('#mainContent');
    const html = `
      <div class="grid" style="grid-template-columns:1fr 1fr; align-items:center;">
        <div class="form-group"><input type="text" id="searchInput" placeholder="Search tasks..." style="width:100%; padding:.5rem;"/></div>
        <div class="form-group"><select id="filterSubject" style="width:100%; padding:.5rem;"><option value="all">All Subjects</option>${state.subjects.map(s=>`<option value="${s.id}">${s.name}</option>`).join('')}</select></div>
      </div>
      <div class="table-container" style="margin-top:1rem;">
        <table class="table" id="tasksTable">
          <thead><tr><th>Title</th><th>Due</th><th>Subject</th><th>Status</th></tr></thead>
          <tbody></tbody>
        </table>
      </div>
    `;
    container.innerHTML = html;
    renderTaskTable(state.tasks);
    $('#searchInput').addEventListener('input', applyFilters);
    $('#filterSubject').addEventListener('change', applyFilters);
  }

  function renderTaskTable(tasks) {
    const tbody = $('#tasksTable tbody');
    tbody.innerHTML = tasks.map(t => {
      const sub = state.subjects.find(s=>s.id===t.subject);
      return `<tr data-id="${t.id}"><td><a href="#" class="task-link">${t.title}</a></td><td>${t.due}</td><td>${sub?sub.name:'-'}</td><td><span class="badge ${t.status}">${t.status}<\/span><\/td><\/tr>`;
    }).join('');
    $$('.task-link').forEach(el => el.addEventListener('click', e=>{e.preventDefault(); openTaskDetail(e.target.closest('tr').dataset.id);}));
  }

  function applyFilters() {
    const query = $('#searchInput').value.toLowerCase();
    const subj = $('#filterSubject').value;
    let filtered = state.tasks;
    if (query) filtered = filtered.filter(t=>t.title.toLowerCase().includes(query));
    if (subj !== 'all') filtered = filtered.filter(t=>t.subject===subj);
    renderTaskTable(filtered);
  }

  function renderSubjects() {
    const container = $('#mainContent');
    const html = `
      <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:1rem;">
        ${state.subjects.map(s=>`<div class="card" style="border-left:4px solid ${s.color};"><h3>${s.name}</h3></div>`).join('')}
      </div>
    `;
    container.innerHTML = html;
  }

  // Task Detail Modal
  function openTaskDetail(id) {
    const task = state.tasks.find(t=>t.id===id);
    if (!task) return;
    state.editingTaskId = id;
    $('#modalTitle').textContent = 'Edit Task';
    $('#taskTitle').value = task.title;
    $('#taskDue').value = task.due;
    populateSubjectSelect($('#taskSubject'), task.subject);
    $('#taskStatus').value = task.status;
    toggleModal(true);
  }

  function populateSubjectSelect(selectEl, selectedId) {
    selectEl.innerHTML = state.subjects.map(s=>`<option value="${s.id}" ${s.id===selectedId?'selected':''}>${s.name}</option>`).join('');
  }

  function toggleModal(show) {
    $('#taskModal').setAttribute('aria-hidden', show ? 'false' : 'true');
  }

  // Add Task Flow
  function openAddTaskModal() {
    state.editingTaskId = null;
    $('#modalTitle').textContent = 'Add Task';
    $('#taskForm').reset();
    populateSubjectSelect($('#taskSubject'));
    toggleModal(true);
  }

  // Form handling
  $('#taskForm').addEventListener('submit', e=>{
    e.preventDefault();
    const title = $('#taskTitle').value.trim();
    const due = $('#taskDue').value;
    const subject = $('#taskSubject').value;
    const status = $('#taskStatus').value;
    if (state.editingTaskId) {
      const task = state.tasks.find(t=>t.id===state.editingTaskId);
      task.title = title; task.due = due; task.subject = subject; task.status = status;
      showToast('Task updated');
    } else {
      const newTask = { id: 't' + Date.now(), title, due, subject, status };
      state.tasks.push(newTask);
      showToast('Task added');
    }
    toggleModal(false);
    renderScreen();
  });
  $('#cancelTaskBtn').addEventListener('click',()=>toggleModal(false));

  // Navigation
  function setActiveNav() {
    $$('.nav-item').forEach(item => {
      item.classList.toggle('active', item.dataset.screen===state.currentScreen);
    });
  }

  $$('#navList .nav-item').forEach(item => {
    item.addEventListener('click',()=>{ state.currentScreen=item.dataset.screen; renderScreen(); });
  });

  $('#globalAddTaskBtn').addEventListener('click', openAddTaskModal);
  $('#menuToggle').addEventListener('click',()=>{
    $('#sidebar').classList.toggle('open');
  });

  // Initialize
  initMock();
  renderScreen();
})();