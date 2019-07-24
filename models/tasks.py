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
                    name = record["name"]
                )
            )
        return values