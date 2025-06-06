from flask import Flask, request
import requests
import json

app = Flask(__name__)

BOT_TOKEN = "7681427635:AAHLK2hvr2ooTiQJV_axXeGRlTffh7-HTKg"
CHAT_ID = "-1002501325876"

@app.route("/", methods=["POST"])
def alert():
    try:
        if request.is_json:
            data = request.get_json()
            message = data.get("message", "⚠️ Alerte vide (JSON)")
        else:
            message = request.data.decode("utf-8")

        # Envoi vers Telegram
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        response = requests.post(url, json=payload)
        return {"status": "ok", "telegram": response.json()}

    except Exception as e:
        return {"status": "error", "details": str(e)}, 400
