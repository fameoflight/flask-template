from flask import Blueprint, jsonify

main_routes = Blueprint('main', __name__)


@main_routes.route('/')
def hello():
    return jsonify({"message": "Hello, World!"})


@main_routes.route('/api/data')
def get_data():
    return jsonify({"data": [1, 2, 3, 4, 5]})
