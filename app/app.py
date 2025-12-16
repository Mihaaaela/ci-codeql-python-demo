from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host")

    if not host:
        return "Missing host parameter", 400

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
    path = request.args.get("path")

    if not path:
        return "Missing path parameter", 400

    # vulnerabilitate: path traversal
    with open(path, "r") as f:
        return f.read()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
