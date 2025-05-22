from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Your actual Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = "7640780711:AAEhYkCOUd9JyPIB62bZ0oaE3uqFvcfnWIA"
TELEGRAM_CHAT_ID = "5311182983"

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    if data is None:
        return 'No data received', 400

    message = data.get('message', 'No message found in payload')

    send_text = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }

    response = requests.post(send_text, json=payload)

    if response.status_code != 200:
        return f"Failed to send message: {response.text}", 500

    return 'OK', 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
