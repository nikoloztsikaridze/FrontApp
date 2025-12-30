from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to call backend

@app.route("/")
def home():
    return jsonify({"message": "Backend is running 🚀"})

@app.route("/hello", methods=["POST"])
def hello():
    data = request.get_json()
    name = data.get("name", "Guest")
    return jsonify({
        "response": f"Hello, {name}! This message came from Python backend 🐍"
    })

if __name__ == "__main__":
    app.run(debug=True)
