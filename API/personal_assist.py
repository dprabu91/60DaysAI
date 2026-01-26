from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Assistant API is running!"

@app.route("/assist", methods=["POST"])
def assist():
    data = request.json
    message = data.get("message", "")

    if "hello" in message.lower():
        reply = "Hello! How can I help you?"
    else:
        reply = "I'm learning. Try something else."

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,        # 👈 IMPORTANT
        use_reloader=False  # 👈 VERY IMPORTANT
    )
