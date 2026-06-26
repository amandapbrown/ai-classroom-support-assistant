from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    feedback = ""

    if request.method == "POST":
        trainee_response = request.form.get("trainee_response")

        feedback = f"""
Good start. You said:

"{trainee_response}"

For this type of issue, strong first checks usually include:
1. Confirm the HDMI/USB-C cable is securely connected.
2. Check that the projector is on the correct input.
3. Verify the laptop detects the external display.
4. Try mirroring/extending the display.
5. Escalate if the issue appears to be hardware-related.

Next step: explain why your first check matters.
"""

    return render_template("index.html", feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)