from flask import Flask
from flask import request

app = Flask("todo-list")
app.debug = True # Enable debug mode


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/hi")
def hi():
    name = request.args.get("name", "Jim")
    return "Hi, %s" % name

if __name__ == "__main__":
    app.run(host="0.0.0.0")
