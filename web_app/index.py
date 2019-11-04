from aiohttp import web
from app.app import App
import json

main = web.Application()

""" Загрузим конфигурационные данные из json файла, с будущем возможно дополнение данных для мастабирования системы """

with open('config.json') as file:
    file = json.load(file)

app = App(file['mongo_con_str'])

main.router.add_route('GET', '/posts', app.get_operation)

web.run_app(main, host=file['host'], port=file['port'])
