from aiohttp import web
from app.mongo_func import MongoFuncs


class App:
    def __init__(self, con_str):
        self.con_str = con_str # строка с данными для подключения к mongo
        self.get_params_list = ['order', 'offset', 'limit'] # список поддерживаемых аттрибутов в get запросе, можно перенести в json для больше гибкости
        self.test = 1 # параметр для инверсии asc/desc сортировки

    def get_operation(self, req):

        params = req.rel_url.query # распарсим запрос от клиента
        mongo_db = MongoFuncs(self.con_str)

        for param in params:

            if param in self.get_params_list:
                mongo_db.check_params(param, params[param]) # если в запросе есть аттрибуты поддерживаемые нашим апи, запишем данные из них

        self.test = -self.test
        posts = mongo_db.get_posts(self.test)

        return web.json_response(status=200, data=posts)
