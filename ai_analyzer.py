
import os
from google import genai

from config import GEMINI_API_KEY, GEMINI_MODEL
from security import load_logs


def analyze_latest_event():

    # Load recorded security events
    logs = load_logs()

    if not logs["events"]:
        print("\nNo security events available for analysis.")
        return

    # Get the latest event
    event = logs["events"][-1]

    # Check API key
    if not GEMINI_API_KEY:
        print("\nGemini API key not found!")
        print("Please configure your .env file.")
        return

    # Get filename without exposing full path
    file_name = os.path.basename(event["file"])

    # Prepare the AI prompt
    prompt = f"""
    You are FileGuard AI, a cybersecurity assistant.

    Analyze this file integrity event.

    File name: {file_name}
    Event type: {event["event"]}
    Risk level: {event["risk"]}
    Timestamp: {event["timestamp"]}

    Explain:

    1. What happened?
    2. Why might this event be concerning?
    3. What should the user do next?
    4. Is this proof of an attack?

    Important rules:
    - Do not assume every modification is malicious.
    - Explain uncertainty clearly.
    - Give practical security recommendations.
    - Use simple language that beginners can understand.
    """

    try:

        # Connect to Gemini
        client = genai.Client(api_key=GEMINI_API_KEY)

        # Generate AI analysis
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        # Display AI response
        print("\n========== GEMINI SECURITY ANALYSIS ==========")
        print(response.text)
        print("==============================================")

    except Exception as error:

        print("\nGemini AI analysis failed.")
        print("Check your API key, internet connection, and model.")
        print("Error:", error)
