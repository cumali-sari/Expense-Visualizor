import os
import requests
from dotenv import load_dotenv
import re

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

def categorize_expense(description):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "user",
                "content": f"Categorize this expense into one of: Food, Transportation, Market, Entertainment, Shopping, Sent Money, Received Money, Bills, Other.\nExpense: {description}"
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
    except Exception:
        return "Other"

    try:
        text = data["choices"][0]["message"]["content"].strip()
        match = re.search(r"(Food|Transportation|Market|Entertainment|Shopping|Sent Money|Received Money|Bills|Other)", text, re.IGNORECASE)
        if match:
            return match.group(0).capitalize()
        else:
            return "Other"
    except Exception:
        return "Other"

