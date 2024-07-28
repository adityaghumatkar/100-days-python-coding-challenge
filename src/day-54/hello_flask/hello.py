from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        ret_value = function()
        return f"<b>{ret_value}</b>"
    return wrapper_function
def make_underlined(function):
    def wrapper_function():
        ret_value = function()
        return f"<u>{ret_value}</u>"
    return wrapper_function



@app.route("/")  # Python decorator
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")  # Python decorator
@make_bold
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>")
def greet(name):
    return f"Hello there {name}"

if __name__ == "__main__":
    app.run(debug=True)
