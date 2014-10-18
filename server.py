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


@app.route("/my_dict")
def my_dict():

    dictionary = {
        "apple": "a fruit with red color.",
        "banana": "a fruit with yellow color.",
        "kiwi": "a fruit with brown color.",
        "melon": "a fruit with green color.",
        "watermelon": "a popular fruit in summer."
    }

    q = request.args.get("q", None)

    if q in dictionary:
        return dictionary[q]
    else:
        return "Not found"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
