from flask import Flask, request
import os

app = Flask(__name__)

# endpoint simplu pentru testare retea
@app.route("/ping")
def ping():
    host = request.args.get("host")

    if host is None:
        return "Missing host parameter", 400

    # construim comanda direct (intentionat nesigur)
    cmd = "ping -c 1 " + host

    try:
        output = os.popen(cmd).read()
    except Exception as e:
        return str(e), 500

    return output


if __name__ == "__main__":
    # rulare locala
    app.run(host="0.0.0.0", port=5000)
