from flask import Flask
from flask import request
from flask import render_template

app = Flask("todo-list")
app.debug = True # Enable debug mode


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/hello")
def hello_many():
    return render_template("hello.txt")


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
