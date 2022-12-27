from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
app.run(debug=True, host="0.0.0.0", port=5000)    
#python3 -m flask --app hello run

