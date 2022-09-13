from pymongo import MongoClient


class Mongo:
    """
    When calling an instance of class returns a database from MongoClient
    """

    def __init__(self, user: str, password: str, db: str):
        self.user = user
        self.password = password
        self.db = db
        self.client = MongoClient(
            'mongodb://mongodb:27017/?authSource=admin&readPreference=secondary&directConnection=true&ssl=false',
            username=self.user,
            password=self.password).fastapi
