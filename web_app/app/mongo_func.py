from app.databases import MongoDB
import random


class MongoFuncs(MongoDB):
    def __init__(self, con_str):
        super().__init__(con_str)

        # обьявим словарь с дефолтными данными для выборки из бд

        self.params = {
            'order': '_id',
            'offset': 0,
            'limit': 5
        }

    def get_posts(self, asc):

        """ Метод для получения данных и бд """

        db = self.connect_to_db('py_test_db')

        posts_count = db.py_test.count()
        data = [{'posts_count': posts_count}]    # добавим количество постов к выводу
        posts = db.py_test.find()\
            .sort(self.params['order'], asc)\
            .skip(abs(int(self.params['offset'])))\
            .limit(abs(int(self.params['limit'])))

        for post in posts:
            data.append(post)

        return data

    def check_params(self, param, param_value):

        """ Метод для записи параметров приходящих в гет запросах клиента """

        if param in self.params.keys():
            self.params[param] = param_value
