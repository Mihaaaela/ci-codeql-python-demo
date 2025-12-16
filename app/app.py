from flask import Flask, request

app = Flask(__name__)

# VULNERABILITATE INTENȚIONATĂ (pentru CodeQL)
@app.route("/hello")
def hello():
    name = request.args.get("name")
    return "Hello " + name

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
