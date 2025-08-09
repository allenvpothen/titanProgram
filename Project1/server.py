from flask import Flask, request, jsonify, send_from_directory
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_folder="public")

@app.route("/")
def serve_index():
    return send_from_directory("public", "index.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("public", path)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    chat = data.get("chat", "")

    prompt = f"""
    You are the Crush-o-Meter.
    Analyze this chat and reply with ONLY one of these categories:
    - "🔥 Rizz"
    - "🧢 Bro Zone"
    - "💀 Cooked"
    - "🤷 Maybe-Maybe Zone"

    Choose the one that best matches the romantic potential in the chat.
    Chat: \"\"\"{chat}\"\"\"
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10
        )

        category = response.choices[0].message["content"].strip()
        return jsonify({"status": category})
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500

if name == "__main__":
    app.run(port=3000, debug=True)