from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Free API for real-time currency exchange rates
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

@app.route('/convert', methods=['GET'])
def convert_currency():
    try:
        amount = float(request.args.get('amount'))
        from_currency = request.args.get('from').upper()
        to_currency = request.args.get('to').upper()

        response = requests.get(API_URL).json()
        rates = response['rates']

        if from_currency not in rates or to_currency not in rates:
            return jsonify({"error": "Invalid currency code"}), 400

        converted_amount = (amount / rates[from_currency]) * rates[to_currency]

        return jsonify({
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
            "converted_amount": round(converted_amount, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
