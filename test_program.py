import requests

url = 'http://127.0.0.1:5000/analyze'
data = {
    "analyze_expense": True,
    "user_id": "12345",
    "month": "11-2024",
    "expenses": [
        {"category": "Food", "amount": 200},
        {"category": "Transport", "amount": 50}
    ]
}

response = requests.post(url, json=data)
print(response.json())