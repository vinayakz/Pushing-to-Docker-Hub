from flask import Blueprint, render_template, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/api/status', methods=['GET'])
def api_status():
    return jsonify({"message": "server is up and running"})

