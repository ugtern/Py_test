import pymongo
import logging


class MongoDB:
    def __init__(self, con_str):
        self.client = pymongo.MongoClient(con_str)

    def connect_to_db(self, db_name):
        try:
            db = self.client[db_name]
        except:
            logging.info('не получилось подключиться к указанной базе данных')
        else:
            return db

    def get_next_id(self, db_name, collection_name):

        db = self.client[db_name]
        result = db.counters.find_and_modify(query={"_id": collection_name},
                                             update={"$inc": {"next": 1}},
                                             upsert=True, new=True)
        return result["next"]