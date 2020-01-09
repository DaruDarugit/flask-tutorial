from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, Wonseon!"

@app.route("/hello")
def hello_world2():
    return "Hello, Wonseon2!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
