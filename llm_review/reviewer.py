import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_review(pr_data, risks):

    prompt = f"""
    Review this pull request.

    Title:
    {pr_data['title']}

    Risks:
    {risks}

    Give:
    1. Summary
    2. Risks
    3. Suggestions
    """

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-oss-20b:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    print(response.json())
    return "done"