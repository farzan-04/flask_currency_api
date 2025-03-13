# Currency Converter API 🌍💰
This is a REST API built with **Flask** that provides real-time currency conversion.

## 🔗 Live API
🚀 **Base URL:** flask-currency-api-2.onrender.com](https://flask-currency-api-2.onrender.com)  


🛠️Tech Stack:
Flask (Backend Framework)
Requests (Fetch real-time exchange rates)
Gunicorn (For deployment)
Render (Hosting)


⚡ Deployment
The API is deployed on Render and is fully functional.

🔗 Live API URL: flask-currency-api-2.onrender.com
🔄 Used by: Currency Converter GUI


📡 **Example Request:**  
https://flask-currency-api-2.onrender.com/convert?amount=100&from=USD&to=INR

📤 **Example Response:**
```json
{
    "from": "USD",
    "to": "INR",
    "amount": 100,
    "converted_amount": 8300.00
}

