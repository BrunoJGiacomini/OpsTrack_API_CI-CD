from flask import Flask

app = Flask(__name__)

@app.route("/route", methods=["GET"])
def route():
    return "Vai Corinthians!"

@app.route("/status")
def status():
    return {
        "status": "ok",
        "version": "1.2.0",
    }

@app.route("/tickets")
def tickets():
    return [
        {
            "id": 1,
            "title": "Erro ao fazer login",
            "status": "aberto"
        },
        {
            "id": 2,
            "title": "Problema no pagamento",
            "status": "em andamento"
        },
        {
            "id": 3,
            "title": "Dúvida sobre cadastro",
            "status": "fechado"
        }
    ]

@app.route("/sobre")
def sobre():
    return {
        "name": "API SCCP",
        "version": "1.2.0",
        "status": "ok"
    }


if __name__ == "__main__":
    app.run(debug=True)
