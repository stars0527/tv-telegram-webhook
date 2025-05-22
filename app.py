from flask import Flask, request
import requests

app = Flask(__name__)

# Replace with your own bot token and chat ID
BOT_TOKEN = "7640780711:AAEhYkCOUd9JyPIB62bZ0oaE3uqFvcfnWIA"
CHAT_ID = "5311182983"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data is None:
        return "No data received", 400

    message = data.get("message", "No message content")
    
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(telegram_url, json=payload)
    
    if response.status_code == 200:
        return "Message sent", 200
    else:
        return f"Failed to send message: {response.text}", 500

@app.route('/')
def home():
    return "Webhook is live!", 200
