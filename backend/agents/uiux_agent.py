import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_uiux(app_brief):

    prompt = f"""
You are a senior UI/UX designer.

Understand the following application requirement and create a practical UI/UX plan
that another frontend engineer can directly implement.

APPLICATION REQUIREMENT:
{app_brief}

Return ONLY valid JSON using exactly this structure:

{{
  "app_name": "",
  "app_description": "",
  "target_users": [],
  "screens": [
    {{
      "name": "",
      "purpose": "",
      "components": [],
      "actions": []
    }}
  ],
  "navigation": {{
    "type": "",
    "items": []
  }},
  "user_flows": [],
  "design_system": {{
    "primary_color": "",
    "secondary_color": "",
    "background_color": "",
    "text_color": "",
    "font": "",
    "style": ""
  }},
  "responsive_behavior": [],
  "frontend_requirements": []
}}

RULES:

- Return complete valid JSON only.
- No markdown.
- No explanations.
- Create 4 to 6 screens.
- Choose screens based on the actual application requirement.
- Do not force unnecessary screens.
- Keep descriptions short.
- Maximum 5 components per screen.
- Maximum 3 actions per screen.
- Maximum 4 target users.
- Maximum 6 navigation items.
- Maximum 4 user flows.
- Maximum 4 responsive behavior items.
- Maximum 6 frontend requirements.
- Do not add fields outside the specified structure.

SCREEN SELECTION:

Understand what type of application this is before selecting screens.

Examples:

- Food/order application:
  Home, categories/menu, product or dish details, cart/orders, account when useful.

- E-commerce:
  Home, products, product details, cart/orders, account when useful.

- Expense/finance:
  Dashboard, transactions, add/edit transaction, reports, settings when useful.

- Education:
  Dashboard, courses/classes, assignments/progress, details, profile when useful.

- Booking:
  Home/search, results, details, booking, bookings/account.

- Healthcare:
  Dashboard, appointments, patients/details, records, profile/settings when useful.

- Productivity:
  Dashboard, tasks/projects, task details, calendar/activity, settings when useful.

- Portfolio:
  Home, about, projects, project details, contact.

These are examples only.

For any other application, create screens that naturally fit the requirement.

Do not add Profile, Settings, Dashboard, Cart, or other common screens unless
they actually make sense for the application.

LAYOUT:

Specify a navigation style appropriate for the application.

Use:
- Sidebar for dashboard/application-style systems when useful.
- Top navigation for websites and simpler applications.
- Appropriate mobile navigation.

DESIGN:

Choose a visual style appropriate for the application's purpose.

Examples:
- Modern SaaS.
- Clean professional.
- E-commerce.
- Food/restaurant.
- Education.
- Finance.
- Healthcare.
- Creative portfolio.

Do not use the same design description for every application.

FUNCTIONALITY:

Describe the important actions the frontend must support.

Examples:
- Add/edit/delete.
- Search/filter.
- Submit forms.
- Add to cart.
- Checkout.
- Book appointment.
- Track status.
- Navigate between screens.
- Save settings.

Only include functionality relevant to the requirement.

VISUAL CONTENT:

If the application naturally benefits from images, mention appropriate visual content.

Examples:
- Food → dishes/categories.
- Shopping → products.
- Travel → destinations.
- Portfolio → project visuals.

If images are not useful, do not require them.

The specification must be concise but provide enough information to build
a polished and functional frontend.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=2000
    )

    content = response.choices[0].message.content.strip()

    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(content)

    except json.JSONDecodeError:
        print("Agent 1 returned invalid JSON.")
        print("Response length:", len(content))
        print("Last 500 characters:")
        print(content[-500:])
        raise