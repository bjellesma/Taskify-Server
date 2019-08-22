from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
import json

# app imports
from models.lists import ListsModel
from models.tasks import TasksModel

api_routes = Blueprint('api_routes', __name__)

@api_routes.route("/api/getlists", methods = ["GET"])
def get_lists(
    limit=None
):
    """
    Get all lists
    """
    limit = request.args.get('limit')
    lists = ListsModel().read_lists(
        limit=limit
    )
    response = jsonify(lists)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@api_routes.route("/api/gettasks", methods=["GET"])
def get_list_tasks(
    limit=None
):
    # id will be the id of the list
    lid = request.args.get('id')
    limit = request.args.get('limit')
    print(f'limit: {limit}')
    if not lid:
        # if no list id was specified
        TasksModel.get_tasks()
    tasks = TasksModel.get_tasks_by_id(lid, limit)
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
    completed = data["completed"]
    list_id = data["list_id"]
    task, task_id = TasksModel.add_task(title, completed, list_id)
    task = {
        "uid": str(task_id),
        "title": str(task["title"]),
        "completed": task["completed"]

    }
    return json.dumps(task)

@api_routes.route("/api/updatetaskcomplete", methods=["PUT"])
@cross_origin()
def update_task():
    data = request.get_json(silent=True)
    task_id = data["task_id"]
    completed = data["completed"]
    print(f'id: {task_id}\ncompleted: {completed}')
    result = TasksModel.update_task_complete(
        task_id=task_id,
        completed=completed
    )
    return ''

@api_routes.route("/api/addlist", methods=["POST"])
@cross_origin()
def add_list():
    # The data is sent as a json object
    data = request.get_json(silent=True)
    name = data["name"]
    user_id = data["user_id"]
    new_list, list_id = ListsModel.add_list(name, user_id)
    new_list = {
        "uid": str(list_id),
        "name": str(new_list["name"])
    }
    return json.dumps(new_list)