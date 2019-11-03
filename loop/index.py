from app.worker import WorkerClass

import json

with open('config.json') as file:
    file = json.load(file)

work = WorkerClass(file['mongo_con_str'], file['url_for_parse'])
work.parse_worker()
