import argparse
import os
import sys
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

API_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent"
)

def ask_ai(error_msg: str) -> str:
    prompt = f"""
You are a senior software engineer.
Given the terminal error below, reply with ONE short sentence
explaining how to fix it. No extra words.

Error:
{error_msg}
"""

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    r = requests.post(
        f"{API_URL}?key={API_KEY}",
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=10
    )

    if r.status_code != 200:
        try:
            error_details = r.json().get("error", {}).get("message", "Unknown error")
            return f"AI request failed ({r.status_code}): {error_details}"
        except Exception:
            return f"AI request failed ({r.status_code}): {r.text}"

    try:
        return r.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except (KeyError, IndexError, TypeError):
        return "Could not parse AI response."

def main():
    if not API_KEY:
        print("Error: GEMINI_API_KEY not set")
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="Fix terminal errors using AI"
    )
    parser.add_argument("error", help="Error message")
    args = parser.parse_args()

    fix = ask_ai(args.error)
    print(f"\nFix: {fix}\n")
