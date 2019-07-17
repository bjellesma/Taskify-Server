from models.mongobase import taskify

class ListsModel():

    @classmethod
    def read_lists(cls):
        """
        read entire lists collection
        """
        values = []
        lists_collection = taskify['lists']
        records = lists_collection.find()
        for record in records:
            values.append(
                dict(
                    uid = str(record["_id"]),
                    name = record["name"]
                )
            )
        return values
        


