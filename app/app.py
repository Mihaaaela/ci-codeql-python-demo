from flask import Flask, request, escape
import subprocess
import os

app = Flask(__name__)


@app.route("/hello")
def hello():
    name = request.args.get("name")
    if not name:
        name = "world"
    return "Hello " + escape(name)


@app.route("/ping")
def ping():
    host = request.args.get("host")

    if not host:
        return "Missing host parameter", 400

    try:
        result = subprocess.run(
            ["ping", "-c", "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        return result.stdout
    except Exception:
        return "Ping failed", 500


@app.route("/read")
def read_file():
    path = request.args.get("path")

    if not path:
        return "Missing path parameter", 400

    base_dir = os.path.abspath("safe_files")
    full_path = os.path.abspath(os.path.join(base_dir, path))

    if not full_path.startswith(base_dir):
        return "Access denied", 403

    try:
        with open(full_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found", 404
    except Exception:
        return "Error reading file", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
