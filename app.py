from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({'data': "working..."})


@app.route("/api")
def api():
    return jsonify({"data": "this api endpoint"})
