from app.databases import MongoDB
import random


class MongoFuncs(MongoDB):
    def __init__(self, con_str):
        super().__init__(con_str)

    def get_posts(self):
        db = self.connect_to_db('py_test_db')
        posts_count = db.py_test.count()
        data = [posts_count]
        for post in db.py_test.find():
            data.append(post)
        return data

    def remove_data(self):
        db = self.connect_to_db('py_test_db')

        deleted = db.py_test.remove({})
        print(deleted)
