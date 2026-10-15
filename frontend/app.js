async function generateApp() {

    const brief = document.getElementById("appBrief").value.trim();
    const button = document.getElementById("generateBtn");
    const status = document.getElementById("status");
    const result = document.getElementById("result");

    if (!brief) {
        status.textContent = "Please describe your application first.";
        return;
    }

    button.disabled = true;
    button.textContent = "Generating...";
    status.textContent = "AI is designing and building your application...";
    result.style.display = "none";

    try {

        const response = await fetch("http://127.0.0.1:8000/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                brief: brief
            })
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();

        if (data.success) {
            status.textContent = "Your application has been generated successfully!";
            result.style.display = "block";
        }

    } catch (error) {

        status.textContent =
            "Could not connect to AppForge AI backend. Make sure the server is running.";

        console.error(error);

    } finally {

        button.disabled = false;
        button.textContent = "Generate App";
    }
}


function previewApp() {
    window.open(
        "http://127.0.0.1:8000/generated/index.html",
        "_blank"
    );
}