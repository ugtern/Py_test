from aiohttp import web
from app.mongo_func import MongoFuncs
import json


class App:
    def __init__(self, con_str):
        self.con_str = con_str

    def get_operation(self, req):
        mongo_db = MongoFuncs(self.con_str)
        posts = mongo_db.get_posts()
        print(posts)
        data = json.dumps(posts)
        return web.json_response(status=200, data=data)
