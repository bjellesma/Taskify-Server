from flask import Blueprint, jsonify
import json

# app imports
from models.lists import ListsModel

api_routes = Blueprint('api_routes', __name__)

@api_routes.route("/api/getlists", methods = ["GET"])
def get_lists():
    """
    Get all lists
    """
    lists = ListsModel().read_lists()
    response = jsonify(lists)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@api_routes.route("/api/getlisttasks", methods=["GET"])
def get_list_tasks():
    list_name = request.args.get('list')
    response = flask.jsonify(list)
    # TODO get tasks with the list name from mongo
    # For now, we are hardcoding the values
    # tasks = get_tasks(list_name)
    
    return json.dumps(tasks)