import os
import json
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()


class AIAnalyst:
    """
    Generates DFIR incident reports using Gemini.
    """

    def __init__(self, investigation: dict):
        self.investigation = investigation

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def analyze(self) -> str:

        investigation_json = json.dumps(
            self.investigation,
            indent=2
        )

        prompt = f"""
You are a senior Digital Forensics and Incident Response (DFIR) analyst.

Analyze the following security investigation:

{investigation_json}

Generate a professional incident report with the following sections:

1. Executive Summary
2. Attack Analysis
3. Indicators of Compromise (IOCs)
4. Risk Assessment
5. Recommended Actions

Rules:
- Use ONLY the investigation data provided.
- Do NOT invent dates, usernames, IP addresses, events, or evidence.
- If information is missing, write "Not Provided".
- Never assume whether an IP address is internal or external.
- Keep the report professional and concise.
"""

        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                return response.text

            except Exception as e:

                # Retry only if Gemini is overloaded
                if "503" in str(e):
                    print(f"\nGemini busy... retrying ({attempt + 1}/3)")
                    time.sleep(5)

                else:
                    return f"""
AI report could not be generated.

Reason:
{e}

The threat detection pipeline completed successfully.
This issue occurred while contacting the external Gemini API.
"""

        return """
AI report could not be generated.

Reason:
Gemini API is currently unavailable after 3 retry attempts.

The threat detection pipeline completed successfully.

Please try again in a few minutes.
"""