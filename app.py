from flask import Flask, render_template, request
import random # used to select a random scenario


app = Flask(__name__)

SCENARIOS = [
#TODO: add scenarios
    {
        # Scenario 1: No Signal on projector / blue screen
        "title": "No Signal / Blue Screen",
        "category": "Display Issues",
        "difficulty": "Easy",
        "description": "An instructor reports a blue screen or no signal on the classroom display.",
        "expected_steps": [
            "Reseat the display cable",
            "Reseat the adapter",
            "Check different sources",
            "If laptop source displays, check whether laptop and PC display cables were swapped",
            "If no sources display, try swapping the display cable with laptop connection",
            "Use a working source for class and inform the supervisor"
        ],

        # Scenario 2: No picture on the projector / black screen
        "title": "No Picture / Black Screen",
        "category": "Display Issues",
        "difficulty": "Easy",
        "description": "An instructor reports that the projector is on, but the screen is black.",
        "expected_steps": [
            "Check that the projector is on",
            "Check that the projector is not muted on the touch/button panel",
            "Reseat the display cable",
            "Reseat the adapted",
            "Check screen sharing settings",
            "On Windows, press Win + P and select Duplicate",
            "On Mac, press Command + F1 or check display settings",
            "Inform supervior if issue continues"
        ],

        # Scenario 3: Loss of audio, program
        "title": "Loss of Program Audio",
        "category": "Audio Issues",
        "difficulty": "Medium",
        "description": "An instructor reports that video is playing, but there is no sound from the classroom speakers.",
        "expected_steps": [
            "Make sure the system is turned on",
            "Check that rack devices are on",
            "Make sure the touch/button panel is on the correct source",
            "Check that audio is not muted on the touch/button panel",
            "Verify the audio output is set to room speakers",
            "Reseat the display cable",
            "If using VGA, reseat the 3.5mm audio cable", 
            "If using Zoom, set audio output to same as System"
        ],

        # Scenario 4: Loss of audio, microphone
        "title": "Loss of Microphone Audio",
        "category": "Microphone Issues",
        "difficulty": "Medium",
        "description": "An instructor reports that the microphone is not working.",
        "expected_steps": [
            "Check if the mic is on",
            "Replace the batteries in the mic if it is off",
            "Make sure the system is turned on",
            "Check that the mic receiver is on and has a group/channel",
            "Mute and unmute the mic on the touch/button panel",
            "Verify the mic group/channel matches the receiver",
            "If using Zoom, check that the correct mic source is selected"
        ],

        # Scenario 5: Document camera issue
        "title": "Document Camera Issue",
        "category": "Document Camera Issues",
        "difficulty": "Easy",
        "description": "An instructor reports that the document camera image is frozen, blurry, black, or missing.",
        "expected_steps": [
            "Check that the touch/button panel is on the correct source",
            "Check that a display cable is plugged into the document camera",
            "If frozen, unplug power from the back, wait 10 seconds, then plug it back in",
            "If blurry, press the AF button to toggle auto-focus",
            "Zoom in or out using the zoom buttons on the document camera to adjust focus",
            "If not powered on, reseat the power cable and make sure the power button is pressed",
            "Inform supervisor if issue continues"
        ],

        # Scenario 6: Frozen Computer
        "title": "Frozen Computer",
        "category": "Computer Issues",
        "difficulty": "Easy",
        "description": "The classroom computer is frozen or not responding to input.",
        "expected_steps": [
            "Check if the mouse and keyboard are working",
            "If there is no response, hard reboot the computer",
            "If there is some response, attempt a soft reboot",
            "If the computer is still frozen, inform the supervisor"
        ],

        # Scenario 7: Frozen Touch/Control Panel
        "title": "Frozen Touch/Control Panel",
        "category": "Control Panel Issues",
        "difficulty": "Advanced",
        "description": "The touch/control panel is frozen or not responding to input.",
        "expected_steps": [
            "Determine whether it is a touch panel or button panel",
            "For a touch panel, check for a small power button and use key/small item to restart it",
            "If accessible, reseat cables behind the panel",
            "Be careful reseating Ethernet cables if Zoom is being used",
            "For a button panel, hold the screen down button for 15-20 seconds", 
            "If the panel is still frozen, inform the supervisor"
        ],

        # Scenario 8: Cannot log in/no network
        "title": "Cannot Log In / No Network",
        "category": "Network Issues",
        "difficulty": "Advanced",
        "description": "An instructor cannot log in to the classroom computer or the computer has no network connection.",
        "expected_steps": [
            "Check for Windows domain error or Mac network indicator",
            "On Mac, check for red or yellow dot in the top right of login screen",
            "Reseat the Ethernet cable behind the computer",
            "Try logging in with the instructor's credentials",
            "Try your own credentials if the instructor's credentials do not work",
            "If your login works, have the instructor contact Help Desk to get their credentials working",
            "If appropriate, check whether a student can log in and use their login for class, never use your own login",
            "If the computer is still not working, inform the supervisor"
        ],

        # Scenario 9: Laptop connection
        "title": "Connecting a Laptop",
        "category": "Laptop Connection Issues",
        "difficulty": "Easy",
        "description": "An instructor is having trouble connecting the laptop to the classroom display.",
        "expected_steps": [
            "Reseat the laptop cable in the laptop port",
            "Check the other end of the laptop cable if accessible",
            "Inspect the cable for bent pins, broken connectors, tears, or bends",
            "Make sure the selected source is a laptop source",
            "If laptop cable is the same type as the main PC display cable, try the PC cable in the laptop and change sources",
            "If using VGA and there is no audio, check the 3.5 mm audio cable",
            "Inform the supervisor if issue continues or if any laptop cables are broken"
        ]
    }


]

@app.route("/", methods=["GET", "POST"])
def home():
    scenario = random.choice(SCENARIOS)
    feedback = ""

    if request.method == "POST":
        trainee_response = request.form.get("trainee_response", "")

        feedback = f"""
Good start! You said: '{trainee_response}'.

For this scenario, some troubleshooting steps may include:
"""

        for step in scenario["expected_steps"]:
            feedback += f"\n- {step}"

        feedback += """

Next step: explain why your first step matters and what you would do next if that step doesn't resolve the issue.
"""

    return render_template(
        "index.html",
        scenario=scenario,
        feedback=feedback,
    )

if __name__ == "__main__":
    app.run(debug=True)