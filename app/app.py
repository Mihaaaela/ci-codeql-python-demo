from flask import Flask, request, escape
import subprocess
import os

app = Flask(__name__)


@app.route("/hello")
def hello():
    name = request.args.get("name", "world")
    return "Hello " + escape(name)


@app.route("/ping")
def ping():
    host = request.args.get("host")

    if not host:
        return "Missing host parameter", 400

    if not host.replace(".", "").isalnum():
        return "Invalid host", 400

    try:
        result = subprocess.run(
            ["ping", "-c", "1", host],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout
    except Exception:
        return "Ping failed", 500


@app.route("/read")
def read_file():
    filename = request.args.get("path")

    if not filename:
        return "Missing path parameter", 400

    base_dir = os.path.abspath("safe_files")
    requested_path = os.path.abspath(os.path.join(base_dir, filename))

    if not requested_path.startswith(base_dir):
        return "Access denied", 403

    try:
        with open(requested_path, "r") as f:
            return f.read()
    except Exception:
        return "File not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
