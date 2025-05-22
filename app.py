import os
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7640780711:AAEhYkCOUd9JyPIB62bZ0oaE3uqFvcfnWIA'
CHAT_ID = '5311182983'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', '⚠️ No message received from TradingView')
    
    telegram_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    
    requests.post(telegram_url, data=payload)
    return 'OK', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
