from flask import Flask, request
from models.lists import ListsModel
import json
import settings 

#route imports
from routes.api import api_routes

app = Flask(__name__)
app.register_blueprint(api_routes)

def get_tasks(task_param):
    """
    # TODO temp
    all hardcoded tasks for testing
    """
    tasks = []
    task_list = [
        {
            'id': 1,
            'list_name': 'critical',
            'task_display': 'Feed the dogs'
        },
        {
            'id': 2,
            'list_name': 'critical',
            'task_display': 'Do not feed the goblin after midnight'
        },
        {
            'id': 3,
            'list_name': 'high',
            'task_display': 'Have fun'
        }
        
    ]
    for task in task_list:
        if task['list_name'] == task_param:
            tasks.append(task)
    return tasks



if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 3001)