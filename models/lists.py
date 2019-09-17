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
    def read_list(cls, lid):
        """
        read specified list
        """
        values = []
        lists_collection = taskify['lists']

        record = lists_collection.find_one(
                {
                    '_id':ObjectId(lid)
                }
            )
        values = dict(
                uid = str(record["_id"]),
                name = record["name"],
                user_id = str(record["user_id"])
            )
        return values

    @classmethod
    def read_lists(cls, uid, limit):
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
            records = lists_collection.find(
                {
                    'user_id':ObjectId(uid)
                }
            ).limit(limit)
        else:
            records = lists_collection.find(
                {
                    'user_id':ObjectId(uid)
                }
            )
        for record in records:
            values.append(
                dict(
                    uid = str(record["_id"]),
                    name = record["name"],
                    user_id = str(record["user_id"])
                )
            )
        return values
        


