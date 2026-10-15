from pathlib import Path
from backend.agents.frontend_agent import generate_frontend

uiux_spec = {
    "app_name": "Student Attendance Tracker",
    "app_description": "A simple website for teachers to manage attendance.",
    "target_users": ["Teachers"],
    "screens": [
        {
            "name": "Dashboard",
            "purpose": "Show attendance overview.",
            "components": ["Header", "Summary cards", "Recent records"],
            "actions": ["View attendance"]
        },
        {
            "name": "Attendance",
            "purpose": "Mark student attendance.",
            "components": ["Student list", "Present/Absent buttons", "Save button"],
            "actions": ["Mark attendance", "Save attendance"]
        },
        {
            "name": "History",
            "purpose": "View previous attendance.",
            "components": ["Date filter", "Records table"],
            "actions": ["Filter records"]
        }
    ],
    "navigation": {
        "type": "sidebar",
        "items": ["Dashboard", "Attendance", "History"]
    },
    "user_flows": [
        "Open Dashboard -> Attendance -> mark students -> save."
    ],
    "design_system": {
        "primary_color": "#2C7A7B",
        "secondary_color": "#68D391",
        "background_color": "#F7FAFC",
        "text_color": "#2D3748",
        "font": "Inter",
        "style": "modern, clean, responsive"
    },
    "responsive_behavior": [
        "Responsive sidebar and stacked mobile layout."
    ],
    "frontend_requirements": [
        "HTML",
        "CSS",
        "JavaScript"
    ]
}

result = generate_frontend(uiux_spec)

generated_folder = Path("generated")
generated_folder.mkdir(exist_ok=True)

(generated_folder / "index.html").write_text(
    result["index_html"],
    encoding="utf-8"
)

(generated_folder / "style.css").write_text(
    result["style_css"],
    encoding="utf-8"
)

(generated_folder / "app.js").write_text(
    result["app_js"],
    encoding="utf-8"
)

print("Agent 2 successful!")
print("HTML length:", len(result["index_html"]))
print("CSS length:", len(result["style_css"]))
print("JS length:", len(result["app_js"]))

print("\nGenerated files:")
print("generated/index.html")
print("generated/style.css")
print("generated/app.js")