from flask import Flask

app = Flask(__name__)

@app.route("/route", methods=["GET"])
def route():
    return "Vai Corinthians!"

@app.route("/status")
def status():
    return {
        "status": "ok",
        "version": "1.0.0",
    }


if __name__ == "__main__":
    app.run(debug=True)
