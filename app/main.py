import os

from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "dev")


@app.route("/health")
def health():
    return jsonify(status="ok", version=VERSION), 200


@app.route("/api/greet/<name>")
def greet(name):
    return jsonify(message=f"Hello, {name}!"), 200


if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8080"))
    print(f"Starting server on http://{host}:{port} ...")
    app.run(host=host, port=port)
