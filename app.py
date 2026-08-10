from flask import Flask

app = Flask(__name__)

@app.route("/route", methods=["GET"])
def route():
    return "Vai Corinthians"

if __name__ == "__main__":
    app.run(debug=True)
