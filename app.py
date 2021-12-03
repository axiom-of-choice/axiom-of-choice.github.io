from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    print("Handling request to home page")
    return render_template('index.html')

@app.route("/me", methods=["GET", "POST"])
def me():
    if request.method == "POST":
        return "Method not available"
    else:
        return render_template("me.html")
if __name__ == '__main__':
    app.run()