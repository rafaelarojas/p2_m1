from flask import Flask, render_template, request, jsonify
from tinydb import TinyDB
import time
from datetime import datetime

db = TinyDB("logs.json")
app = Flask(__name__)

@app.route("/ping")
def ping():
    ping = ({
    "ip": request.remote_addr,
    "metodo":request.method,
    "timestamp": str(datetime.now()),
    "rota": "ping",
    })

    db.insert(ping)

    return {"resposta": "pong"}

@app.route("/echo", methods=["POST"])
def echo():
    banco = request.json
    texto = banco.get("dados")

    echo = {
        "ip": request.remote_addr,
        "metodo": request.method,
        "timestamp": str(datetime.now()),
        "rota": "echo",
        "resposta": texto,
    }

    db.insert(echo)

    return {"resposta": texto}

@app.route("/dash")
def dash():
    return render_template("dash.html")

@app.route("/info")
def info():
    banco = db.all()
    return render_template("info.html", banco=banco)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)