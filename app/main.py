from flask import Flask, jsonify
import os

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "dev")


@app.route("/health")
def health():
    return jsonify(status="ok", version=VERSION), 200


@app.route("/api/greet/<name>")
def greet(name):
    return jsonify(message=f"Hello, {name}!"), 200


if __name__ == "__main__":
    print("Starting server on http://127.0.0.1:8080 ...")
    app.run(host="0.0.0.0", port=8080)
