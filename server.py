from flask import Flask


app = Flask("todo-list")
app.debug = True # Enable debug mode


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
