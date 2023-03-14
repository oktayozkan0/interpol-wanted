from pymongo import MongoClient
import os


mongo_user = os.environ.get("MONGO_API_USER")
mongo_pass = os.environ.get("MONGO_API_PASS")
mongo_port = os.environ.get("MONGO_PORT")
mongo_db = os.environ.get("MONGO_DB")

class DBMongo:
    def __init__(self) -> None:
        conn = MongoClient(f"mongodb://{mongo_user}:{mongo_pass}@mongodb:{mongo_port}/{mongo_db}")
        self.db = conn[mongo_db]

    def get_db(self):
        return self.db

