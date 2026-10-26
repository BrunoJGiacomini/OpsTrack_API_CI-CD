from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def raiz():
    return {
        "servico": "OpsTrack API",
        "status": "online"
    }, 200


@app.route("/route", methods=["GET"])
def route():
    return "Vai Corinthians!"


@app.route("/status", methods=["GET"])
def status():
    return {
        "status": "ok"
    }


@app.route("/version", methods=["GET"])
def version():
    return {
        "version": "1.2.0"
    }


@app.route("/tickets", methods=["GET"])
def tickets():
    return jsonify({
        "tickets": [
            {
                "id": 1,
                "titulo": "Erro ao fazer login",
                "status": "aberto"
            },
            {
                "id": 2,
                "titulo": "Problema no pagamento",
                "status": "em andamento"
            },
            {
                "id": 3,
                "titulo": "Dúvida sobre cadastro",
                "status": "fechado"
            }
        ]
    }), 200


@app.route("/usuarios", methods=["GET"])
def usuarios():
    return jsonify({
        "usuarios": [
            {"id": 1, "nome": "Ana"},
            {"id": 2, "nome": "Carlos"}
        ]
    }), 200


@app.route("/sobre", methods=["GET"])
def sobre():
    return {
        "name": "API SCCP",
        "version": "1.2.0",
        "description": "API para gerenciamento e consulta de dados do SCCP.",
        "status": "ok",
        "environment": "production",
        "author": "Equipe SCCP",
        "documentation": "/docs",
        "endpoints": {
            "sobre": "/sobre",
            "health": "/health",
            "usuarios": "/usuarios"
        }
    }


if __name__ == "__main__":
    app.run(debug=True)
