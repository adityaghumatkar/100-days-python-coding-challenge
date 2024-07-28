from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


random_num = random.randint(0, 9)


@app.route("/<int:number>")
def check(number):
    if number == random_num:
        return f"<h2>and {number} is just right</h2>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif number > random_num:
        return f"<h2>Too high, try again!</h2>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return f"<h2>Too low, try again!</h2>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
