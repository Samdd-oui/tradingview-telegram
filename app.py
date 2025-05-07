@app.route("/", methods=["POST"])
def alert():
    try:
        raw_data = request.data.decode("utf-8")
        print("RAW DATA:", raw_data)

        if request.is_json:
            data = request.get_json()
        else:
            data = json.loads(raw_data)

        message = data.get("message", "⚠️ Alerte reçue, mais sans message clair.")

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        response = requests.post(url, json=payload)
        return {"status": "ok", "telegram": response.json()}

    except Exception as e:
        return {"status": "error", "details": str(e)}, 400
