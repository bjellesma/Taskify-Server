from models.mongobase import taskify
from bson import ObjectId

class ListsModel():

    @classmethod
    def add_list(
        cls,
        name,
        user_id
    ):
        """
        add list through pymongo
        """
        lists_collection = taskify['lists']
        new_list = {
            "name": name,
            "user_id": ObjectId(user_id)
        }
        list_id = lists_collection.insert_one(new_list).inserted_id
        return new_list, list_id

    @classmethod
    def read_lists(cls, limit):
        """
        read entire lists collection
        """
        values = []
        lists_collection = taskify['lists']
        if limit:
            try:
                limit = int(limit)
            except Exception as err:
                print(f'error: {err}')
            records = lists_collection.find().limit(limit)
        else:
            records = lists_collection.find()
        for record in records:
            values.append(
                dict(
                    uid = str(record["_id"]),
                    name = record["name"]
                )
            )
        return values
        


