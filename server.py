from flask import Flask, request
import models.mongobase
import json
import settings 
app = Flask(__name__)

def get_tasks(task_param):
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

@app.route("/api/getlisttasks", methods=["GET"])
def get_list_tasks():
    list_name = request.args.get('list')
    # TODO get tasks with the list name from mongo
    # For now, we are hardcoding the values
    tasks = get_tasks(list_name)
    return json.dumps(tasks)

if __name__ == "__main__":
    print(settings.PORT)
    app.run(host = '0.0.0.0', port = 3001)