from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/hello")
def hello():
    user_name = request.args.get("name")

    if not user_name:
        return "Hello!", 200

    safe_name = escape(user_name)
    return f"Hello {safe_name}", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
