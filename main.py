from flask import Flask, jsonify
import os
from src.services import report_service


ENV_PORT = os.environ.get('PORT', 5000)

app = Flask(__name__)

@app.route("/")
def index():
    return "String"

@app.route("/api/v1/trigger_report", methods=['POST'])
def generate_report():
    return jsonify(report_service.generate_report())

@app.route("/api/v1/get_report/<report_id>")
def get_report(report_id):
    return jsonify(report_service.get_report(report_id))
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=ENV_PORT, debug=True)
