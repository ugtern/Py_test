from aiohttp import web
from app.mongo_func import MongoFuncs
import logging


class App:

    logging.basicConfig(filename='log.log', level=logging.DEBUG)

    def __init__(self, con_str):
        self.con_str = con_str # строка с данными для подключения к mongo
        self.get_params_list = {
            'order': str, 'offset': int, 'limit': int
        } # список поддерживаемых аттрибутов в get запросе, можно перенести в json для больше гибкости
        self.test = 1 # параметр для инверсии asc/desc сортировки

    def get_operation(self, req):

        params = req.rel_url.query # распарсим запрос от клиента
        mongo_db = MongoFuncs(self.con_str)

        """ Добавил сложную систему проверки типов входящих данных, заточка под возможное масштабирование и вхождение данных из разных источников, в разных форматах """

        for param in params:
            if param in self.get_params_list.keys() and type(params[param]) == self.get_params_list[param]: # проверим, поддерживается ли обработка пришедшего нам параметра на сервере, и проверим его тип данных
                mongo_db.check_params(param, params[param]) # если в запросе есть аттрибуты поддерживаемые нашим апи, запишем данные из них
            elif param in self.get_params_list.keys() and type(params[param]) != self.get_params_list[param]:
                try:
                    param_new = self.get_params_list[param](params[param])
                except:
                    logging.info('не удается привести параметр к указанному типу')
                    # здесь можно вставить вывод ошибки и действия при ее возникновению для оповещения пользователя о том что она указал не правильные данные
                else:
                    mongo_db.check_params(param, param_new)


        self.test = -self.test
        posts = mongo_db.get_posts(self.test)

        return web.json_response(status=200, data=posts)
