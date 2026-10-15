import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_frontend(uiux_spec):

    prompt = f"""
You are a senior frontend engineer and product UI designer.

Build a polished, responsive and functional frontend from the following UI/UX
specification.

UI/UX SPECIFICATION:
{json.dumps(uiux_spec, separators=(",", ":"))}

Return ONLY valid JSON:

{{
  "index_html": "",
  "style_css": "",
  "app_js": ""
}}

TECHNOLOGY:

- HTML5
- CSS3
- Vanilla JavaScript
- No React
- No TypeScript
- No frameworks
- No external libraries
- No external fonts
- The application must work locally.

YOUR MAIN GOAL:

Create a frontend that looks like a real modern application, not a demo page.

The interface must be:

- Attractive.
- Clean.
- Functional.
- Responsive.
- Easy to understand.
- Appropriate for the application domain.
- Visually balanced.
- Consistent across all screens.

IMPORTANT:

Do NOT blindly use the same layout for every application.

Use the UI/UX specification and application domain to decide the best layout.

APPLICATION STRUCTURE:

For application-style systems, use:

- Navigation.
- Header/topbar.
- Main content area.
- Screen-based navigation.

For websites or simpler applications, use an appropriate top navigation
or other suitable structure.

Follow the navigation style specified by Agent 1.

LAYOUT:

Use CSS Grid and Flexbox appropriately.

Avoid:

- Overly wide forms.
- Huge empty areas.
- Everything being stacked vertically.
- Every card being full width.
- Excessive text.
- Random decorative elements.
- Overcrowded layouts.

Use:

- Responsive grids.
- Cards.
- Sections.
- Two-column layouts when useful.
- Proper content widths.
- Consistent spacing.
- Clear visual hierarchy.

DASHBOARD:

If the application has a dashboard:

Create a useful dashboard rather than an empty page.

Use domain-appropriate elements such as:

- KPI/stat cards.
- Recent activity.
- Tables.
- Charts or CSS-based visualizations.
- Progress indicators.
- Quick actions.
- Status summaries.

Do not add irrelevant statistics simply to fill space.

For example:

Expense app:
- Spending.
- Budget.
- Categories.
- Recent transactions.

Food app:
- Orders.
- Popular dishes.
- Categories.
- Recent orders.

Education:
- Courses.
- Progress.
- Upcoming assignments.
- Recent activity.

Banking:
- Balance.
- Transactions.
- Spending.
- Account activity.

Choose only elements that make sense.

CARDS:

Cards should have a clear purpose.

Use:

- Good padding.
- Consistent border radius.
- Subtle borders/shadows.
- Clear headings.
- Supporting information.
- Appropriate actions.

Do not create many empty cards.

FORMS:

Forms must look like real application forms.

- Use labels.
- Use suitable input types.
- Group related fields.
- Use sensible widths.
- Use two columns when appropriate.
- Use one column on mobile.
- Clearly distinguish primary and secondary buttons.
- Show success/error feedback where useful.
- Do not stretch a small form across the entire screen.

DATA:

When the application contains data such as:

- Transactions.
- Orders.
- Users.
- Products.
- Students.
- Appointments.
- Tasks.
- Records.

Use appropriate presentation:

- Tables.
- Structured rows.
- Cards.
- Timeline.
- Status badges.
- Summary sections.

Do not display important data as a plain bullet list.

Use realistic sample data relevant to the application.

SEARCH AND FILTER:

If the application naturally needs search or filtering:

- Add a search field.
- Add useful filter controls.
- Make them functional with the mock data.

Do not add search/filter where it is unnecessary.

FUNCTIONALITY:

The frontend must actually work using local/mock JavaScript data.

Implement relevant functionality such as:

- Navigation.
- Add.
- Edit.
- Delete.
- Search.
- Filter.
- Form submission.
- Status changes.
- Cart updates.
- Quantity changes.
- Calculations.
- Tabs.
- Modal dialogs.
- Notifications.
- Save/update actions.

Only implement features relevant to the requirement.

When an action is performed, provide visible feedback.

Do not make buttons that do nothing when they are expected to perform an action.

STATE:

Use JavaScript state for application interactions where useful.

For example:

- Cart items.
- Tasks.
- Transactions.
- Orders.
- Form data.
- Filters.
- Selected items.

Use localStorage when useful for maintaining simple user changes after refresh.

Do not create a backend or database.

SCREEN IMPLEMENTATION:

Every screen in the UI/UX specification MUST be implemented.

Do not omit screens.

Do not add unrelated screens.

Every screen should contain meaningful UI.

Avoid screens containing only:

<h1>...</h1>
<p>...</p>

Each screen should have appropriate components, spacing and content.

NAVIGATION:

- Navigation must work without page reload.
- Active navigation item must be visually clear.
- Screen transitions should be clean.
- Mobile navigation must remain usable.

PROFILE / ACCOUNT:

If a Profile or Account screen exists in the specification:

Create a complete account interface.

Use appropriate information such as:

- Name.
- Email.
- Phone.
- Address.
- Avatar/initials.
- Account settings.

Only include fields relevant to the application.

Do not force a profile screen into applications that do not have one.

IMAGES AND VISUAL MEDIA:

Only use images when they genuinely improve the application.

Good examples:

Food:
- Dish images.
- Category visuals.

Shopping:
- Product images.

Travel:
- Destination images.

Hotels:
- Property/room images.

Portfolio:
- Project visuals.

Do NOT add random images to applications that don't need them.

IMAGE RELEVANCE:

Every image must match the content it represents.

For example:

- A pizza card should show pizza.
- A burger card should show a burger.
- A laptop product should show a laptop.
- A travel destination should show that type of destination.

Never use:

- Random people.
- Unrelated landscapes.
- Random buildings.
- Profile photos as product images.
- Unrelated stock photography.

If a relevant external image cannot be reliably provided:

Use a polished CSS-based or emoji-based placeholder that matches the
application domain.

This is better than showing an unrelated image.

IMAGE FALLBACK:

Every external image must have a graceful fallback.

Use:

- onerror.
- CSS placeholder.
- Emoji.
- Initials.
- Domain-specific visual.

Never show a broken-image icon.

Keep image containers consistent.

FOOD-SPECIFIC RULE:

For food applications, food cards should visually represent the actual food.

Do not use random images just because they are available.

If no reliable dish image is available, use an attractive food-specific
placeholder instead.

RESPONSIVE DESIGN:

The application must work on:

- Desktop.
- Tablet.
- Mobile.

Desktop:

- Use space effectively.
- Use grids and columns where appropriate.

Tablet:

- Reduce columns.
- Maintain readable spacing.

Mobile:

- Use one-column layouts where necessary.
- Keep buttons usable.
- Prevent unwanted horizontal scrolling.
- Make navigation accessible.
- Make tables responsive.

VISUAL DESIGN:

Create a professional design system.

Use CSS variables for:

- Primary color.
- Secondary color.
- Background.
- Surface.
- Text.
- Muted text.
- Border.
- Radius.
- Shadow.

Use consistent:

- Typography.
- Spacing.
- Button styles.
- Card styles.
- Form styles.
- Badge styles.

Use hover and focus states.

Do not use excessive gradients or decorative effects.

Do not make every section look identical.

Make the design appropriate to the domain.

ACCESSIBILITY:

Use:

- Semantic HTML.
- Proper labels.
- Buttons for actions.
- Accessible form controls.
- Sufficient contrast.
- Clear focus states.
- Meaningful button text.

CSS:

Use:

box-sizing: border-box;

Make sure:

- No sidebar overlaps content.
- No content extends outside the viewport.
- Long text wraps.
- Forms don't overflow.
- Images maintain aspect ratio.
- Cards remain usable at different widths.

Use reusable classes such as:

.app
.sidebar
.main
.topbar
.content
.card
.grid
.stat-card
.btn
.badge
.form-group
.table-container
.modal
.toast
.media-card
.image-placeholder

JAVASCRIPT:

Keep JavaScript organized.

Prefer reusable functions such as:

- renderScreen()
- renderCards()
- renderTable()
- showToast()
- handleFormSubmit()
- updateState()

Do not create unnecessary complexity.

OUTPUT:

- Return complete HTML.
- Return complete CSS.
- Return complete JavaScript.
- Do not return markdown.
- Do not explain anything.
- Return valid JSON only.

QUALITY PRIORITY:

Prioritize the following in this order:

1. Functional correctness.
2. Matching the user's requirement.
3. Good layout and usability.
4. Attractive visual design.
5. Responsive behavior.
6. Relevant visual media.
7. Extra decorative details.

Do not sacrifice functionality just to make the interface visually complex.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=7000,
        reasoning_effort="low"
    )

    content = response.choices[0].message.content

    if not content:
        raise RuntimeError("Agent 2 received an empty response from Groq.")

    content = content.strip()

    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(content)

    except json.JSONDecodeError:
        print("Agent 2 returned invalid JSON.")
        print("Response length:", len(content))
        print("Last 500 characters:")
        print(content[-500:])
        raise