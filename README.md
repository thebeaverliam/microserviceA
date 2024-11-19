# Expense Analysis Microservice

## Overview
This microservice analyzes monthly expenses, categorizes them by type, calculates the total amount spent for a given month, and provides spending recommendations based on the categorized data.

## Communication Contract

### Request Data

To request an expense analysis, send a POST request to the `/analyze` endpoint.

#### Example Request
```python
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
```
### Request Parameters

- **analyze_expense** (boolean): Set to `true` to initiate analysis.
- **user_id** (string): Unique identifier for the user.
- **month** (string): The month to analyze, formatted as `MM-YYYY`.
- **expenses** (list of objects): Each expense entry should include:
  - **category** (string): Category name of the expense (e.g., "Food", "Transport").
  - **amount** (number): Amount spent in this category.

### Response Data

The microservice responds with a JSON object containing the analysis results.

### Example Response
```python
{
    "status": "success",
    "categorized_expenses": {
        "Food": 200,
        "Transport": 50
    },
    "monthly_total": 250,
    "recommendations": [
        "Consider reducing spending on dining out to save $50 monthly",
        "Consider using public transport to save on fuel costs"
    ]
}
```

### Response Fields

- **status** (string): Indicates the success or failure of the request.
- **categorized_expenses** (object): A dictionary categorizing expenses by type (e.g., `"Food": 200`).
- **monthly_total** (number): Total amount spent for the specified month.
- **recommendations** (array): Optional list of suggestions for optimizing spending, based on the analysis.

# Setup and Installation
## Install Flask:
```python
pip install flask
```
## Run the Microservice:
```python
python microservice.py
```
## Testing the Microservice:
You can use curl, Postman, or a custom test script like test_program.py to make requests and verify responses.

# Additional Information

Error Handling: If any required fields are missing or analyze_expense is not set to true, the microservice will return a JSON response with "status": "failure" and an appropriate error message.

Port Configuration: The microservice runs by default on http://127.0.0.1:5000. Adjust the URL in test requests if you modify the default port.


# UML Sequence Diagram
![image](https://github.com/user-attachments/assets/6d22bdf7-7dd4-4207-8892-c9f45fae5651)
