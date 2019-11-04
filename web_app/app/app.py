from aiohttp import web
from app.mongo_func import MongoFuncs


class App:
    def __init__(self, con_str):
        self.con_str = con_str
        self.get_params_list = ['order', 'offset', 'limit']
        self.test = 1

    def get_operation(self, req):

        params = req.rel_url.query
        mongo_db = MongoFuncs(self.con_str)

        for param in params:

            if param in self.get_params_list:
                mongo_db.check_params(param, params[param])
                self.test = -self.test

        posts = mongo_db.get_posts(self.test)

        return web.json_response(status=200, data=posts)
