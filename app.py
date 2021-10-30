from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    print("Handling request to home page")
    return render_template('index.html')
