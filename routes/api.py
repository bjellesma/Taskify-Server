from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
import json

# app imports
from models.lists import ListsModel
from models.tasks import TasksModel

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


@api_routes.route("/api/gettasks", methods=["GET"])
def get_list_tasks():
    # id will be the id of the list
    lid = request.args.get('id')
    tasks = TasksModel.get_tasks_by_id(lid)
    response = jsonify(tasks)
    response.headers.add('Access-Control-Allow-Origin', '*')
    # TODO get tasks with the list name from mongo
    # For now, we are hardcoding the values
    # tasks = get_tasks(list_name)
    
    return response

@api_routes.route("/api/addtask", methods=["POST"])
@cross_origin()
def add_task():
    # The data is sent as a json object
    data = request.get_json(silent=True)
    title = data["title"]
    completed = data["title"]
    list_id = data["list_id"]
    task, task_id = TasksModel.add_task(title, completed, list_id)
    task = {
        "uid": str(task_id),
        "title": str(task["title"]),
        "completed": str(task["completed"])

    }
    return json.dumps(task)