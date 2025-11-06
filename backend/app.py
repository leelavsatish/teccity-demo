from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend requests

USERS = {"user1": "pass1", "user2": "pass2"}
VISITS = {"user1": 0, "user2": 0}

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in USERS and USERS[username] == password:
        return jsonify({"status": "success", "message": f"Welcome {username}!"})
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401

@app.route("/api/visits/<username>", methods=["GET"])
def visits(username):
    if username in VISITS:
        VISITS[username] += 1
        return jsonify({"username": username, "visits": VISITS[username]})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

