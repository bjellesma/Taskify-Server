from models.mongobase import taskify
from bson import ObjectId

class TasksModel():

    @classmethod
    def get_tasks_by_id(cls, lid, limit):
        """
        read entire lists collection
        """
        values = []
        tasks_collection = taskify['tasks']
        if limit:
            try:
                limit = int(limit)
            except Exception as err:
                print(f'error: {err}')
            records = tasks_collection.find(
                {
                    'list_id':ObjectId(lid)
                }
            ).limit(limit)
        else:
            records = tasks_collection.find(
                {
                    'list_id':ObjectId(lid)
                }
            )
        records = tasks_collection.find(
            {
                'list_id':ObjectId(lid)
            }
        ).limit(limit)
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
        """
        Update complete status on task

        ! test comment
        :param: task_id
        """
        tasks_collection = taskify['tasks']
        
        query = {'_id': ObjectId(task_id)}
        params = { "$set": {'completed': completed}}
        print(f'query: {query}\nParams: {params}')
        result = tasks_collection.update_one(query, params)
        print(result)
        return result
