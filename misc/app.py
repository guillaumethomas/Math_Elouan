from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route("/hello")
def hello():
    return  "Hello, World"

@app.route("/elouan")
def elouan():
    return "Elouan"

if __name__ == "__main__":
    app.run()

