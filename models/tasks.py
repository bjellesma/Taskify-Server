from models.mongobase import taskify
from bson import ObjectId

class TasksModel():

    @classmethod
    def get_tasks_by_id(cls, lid):
        """
        read entire lists collection
        """
        values = []
        tasks_collection = taskify['tasks']
        records = tasks_collection.find({'list_id':ObjectId(lid)})
        for record in records:
            values.append(
                dict(
                    uid = str(record["_id"]),
                    title = record["title"],
                    completed = record["completed"]
                )
            )
        return values

    @classmethod
    def add_task(
        cls,
        title,
        completed,
        list_id
    ):
        """
        add task through pymongo
        """
        tasks_collection = taskify['tasks']
        task = {
            "title": title,
            "completed": completed,
            "list_id": ObjectId(list_id)
        }
        task_id = tasks_collection.insert_one(task).inserted_id
        return task, task_id

    @classmethod
    def update_task_complete(
        cls,
        task_id,
        completed
    ):
        tasks_collection = taskify['tasks']
        """
        Update complete status on task
        """
        query = {'_id': ObjectId(task_id)}
        params = { "$set": {'completed': completed}}
        print(f'query: {query}\nParams: {params}')
        result = tasks_collection.update_one(query, params)
        print(result)
        return result
