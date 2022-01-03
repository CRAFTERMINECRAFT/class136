from flask import Flask, jsonify, request
from data import final

app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "data": final,
        "message": "SUCCESS!"
    }),200

@app.route("/planet")

def planet():
    name = request.args.get("name")
    planet_data = next(item for item in final if item["name"] == name)
    return jsonify({
        "data": planet_data
    }),200

if __name__ == "__main__":
    app.run()