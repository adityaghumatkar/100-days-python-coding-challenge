from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login_function():
    if request.method == "POST":
        un = request.form["username"]
        pw = request.form["password"]
        print(f"{un}:{pw}")
        return f"<h1>{un}:{pw}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
