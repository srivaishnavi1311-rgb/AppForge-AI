# AppForge-AI
AI-powered frontend application generator using a two-agent architecture.
# AppForge-AI 🚀
### AI-Powered Frontend Application Generator

AppForge-AI is an AI-powered application generator that transforms natural-language requirements into frontend applications using a two-agent architecture. It combines UI/UX planning with AI-generated frontend code to simplify the process of building web interfaces.

## ✨ Key Features

- **Two-Agent Architecture:** Separates UI/UX planning from frontend code generation.
- **AI-Powered UI/UX Planning:** Agent 1 converts user requirements into structured JSON describing the application interface.
- **Automated Frontend Generation:** Agent 2 uses Agent 1's structured output to generate frontend code.
- **Frontend Code Generation:** Generates HTML, CSS, and JavaScript files.
- **Live Browser Preview:** Preview generated applications locally in a web browser.
- **FastAPI Backend:** Provides an API endpoint to process requirements and coordinate both agents.
- **Groq Integration:** Uses a Groq-hosted language model to power AI generation.

## 🏗️ System Architecture

```text
User Requirements
       |
       v
  FastAPI Backend
       |
       v
  Agent 1: UI/UX Planner
       |
       v
  Structured JSON Output
       |
       v
  Agent 2: Frontend Generator
       |
       v
  Generated HTML, CSS, JavaScript
       |
       v
  Browser Preview
```

**Design principle:** Agent 2 receives the structured output from Agent 1 rather than the original user requirements directly. This separates interface planning from code generation.

## 🛠️ Technology Stack

| Component | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| AI Integration | Groq API |
| Frontend | HTML, CSS, JavaScript |
| Development Server | Uvicorn |
| Configuration | Environment variables |

## 📁 Project Structure

```text
AppForge-AI/
├── backend/
│   ├── agents/
│   │   ├── frontend_agent.py
│   │   └── uiux_agent.py
│   ├── schemas/
│   │   └── models.py
│   ├── services/
│   │   └── groq_client.py
│   └── main.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── generated/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── test_agent1.py
├── test_agent2.py
├── test_groq.py
├── .gitignore
└── README.md
```

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/srivaishnavi1311-rgb/AppForge-AI.git
cd AppForge-AI
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install fastapi uvicorn groq python-dotenv
```

If the project uses additional Python packages, install those dependencies as well.

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own API key. Never commit your `.env` file or expose your API key publicly.

### 5. Start the application

From the project root, run:

```bash
uvicorn backend.main:app --reload
```

Open the API documentation in your browser:

http://127.0.0.1:8000/docs

If the frontend is served by the backend, open the application's configured frontend URL. The generated output can be previewed at:

http://127.0.0.1:8000/generated/index.html

The preview URL assumes the backend serves the `generated` directory at `/generated/`.

## 🧪 Testing

The repository includes test scripts for the UI/UX agent, frontend agent, and Groq integration.

```bash
python test_agent1.py
python test_agent2.py
python test_groq.py
```

**Note:** Tests that call the Groq API may consume API usage. Ensure your API key and usage limits are configured before running them.

## 🔐 Security

- Store API keys in environment variables.
- Keep `.env` and virtual environment directories out of version control.
- Never publish API keys, passwords, or other secrets in source code.

## 🎯 Project Objective

The goal of AppForge-AI is to simplify frontend development by dividing the process into two focused AI tasks: interface planning and code generation. This modular architecture provides a foundation for building and improving AI-assisted web application development workflows.

## 👩‍💻 Developer

**Sri Vaishnavi and Deepiga**

B.Tech Artificial Intelligence and Data Science Student

GitHub: [srivaishnavi1311-rgb](https://github.com/srivaishnavi1311-rgb)

---

If you find this project interesting, feel free to explore the repository and its implementation.
