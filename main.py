from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def startPage():
    return "<h1>Welcome to the Student management app</h1>"

@app.route("/welcome")
def welcomePage():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run()