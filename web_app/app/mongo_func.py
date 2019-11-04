from app.databases import MongoDB
import random


class MongoFuncs(MongoDB):
    def __init__(self, con_str):
        super().__init__(con_str)
        self.params = {
            'order': '',
            'offset': 0,
            'limit': 5
        }

    def get_posts(self, asc):
        db = self.connect_to_db('py_test_db')

        posts_count = db.py_test.count()
        data = [posts_count]    # добавим количество постов к выводу

        for post in db.py_test.find()\
                .sort(self.params['order'], asc)\
                .skip(abs(int(self.params['offset'])))\
                .limit(abs(int(self.params['limit']))):

            data.append(post)

        return data

    def check_params(self, param, param_value):
        if param in self.params.keys():
            self.params[param] = param_value
