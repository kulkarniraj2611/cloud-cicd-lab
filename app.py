from flask import Flask

app = Flask(__name__)

DATA = {"name": "Raj"}
DATA["course"] = "Cloud Computing and DevOps"

@app.route("/")
def home():
    return "Welcome to Cloud Computing Lab"

@app.route("/student")
def student():
    return DATA

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
