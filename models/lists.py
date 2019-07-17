from models.mongobase import taskify

class ListsModel():

    @classmethod
    def read_lists(cls):
        """
        read entire lists collection
        """
        lists_collection = taskify['lists']
        return lists_collection.find_one()

