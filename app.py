from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7681427635:AAHLK2hvr2ooTiQJV_axXeGRlTffh7-HTKg"
CHAT_ID = "-1002501325876"  # ID de ton canal Telegram

@app.route("/", methods=["POST"])
def alert():
    data = request.get_json()
    message = data.get("message", "⚠️ Alerte TradingView sans message")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, json=payload)
    return {"status": "ok", "telegram": response.json()}
