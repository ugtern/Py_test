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
