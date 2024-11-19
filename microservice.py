from flask import Flask, request, jsonify

app = Flask(__name__)

def analyze_expenses(data):
    expenses = data.get('expenses', [])
    
    categorized_expenses = {}
    total_expense = 0
    
    for expense in expenses:
        category = expense.get('category')
        amount = expense.get('amount', 0)
        categorized_expenses[category] = categorized_expenses.get(category, 0) + amount
        total_expense += amount

    recommendations = generate_recommendations(categorized_expenses)
    
    response = {
        "status": "success",
        "categorized_expenses": categorized_expenses,
        "monthly_total": total_expense,
        "recommendations": recommendations
    }
    
    return response

def generate_recommendations(categorized_expenses):
    recommendations = []
    
    if categorized_expenses.get("Food", 0) > 150:
        recommendations.append("Consider reducing spending on dining out to save $50 monthly")

    if categorized_expenses.get("Transport", 0) > 100:
        recommendations.append("Consider using public transport or carpooling to save on fuel costs")
    
    if categorized_expenses.get("Entertainment", 0) > 75:
        recommendations.append("Limit streaming services or movie outings to save $30 monthly")

    if categorized_expenses.get("Shopping", 0) > 100:
        recommendations.append("Consider reducing non-essential purchases to save $40 monthly")

    if categorized_expenses.get("Utilities", 0) > 150:
        recommendations.append("Reduce energy usage or switch to energy-saving bulbs to lower utility bills")

    if categorized_expenses.get("Health", 0) > 100:
        recommendations.append("Look into local gym discounts or online workouts to save on fitness expenses")
    
    if categorized_expenses.get("Miscellaneous", 0) > 50:
        recommendations.append("Reevaluate miscellaneous spending to identify areas for possible savings")

    return recommendations


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    
    if data.get("analyze_expense"):
        result = analyze_expenses(data)
        return jsonify(result), 200
    else:
        return jsonify({"status": "failure", "message": "Invalid request or operation not specified"}), 400

if __name__ == '__main__':
    app.run(debug=True)