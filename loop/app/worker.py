import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from app.databases import MongoDB
import logging


class WorkerClass(MongoDB):

    logging.basicConfig(filename='log.log', level=logging.DEBUG)

    def __init__(self, con_str, url):
        super().__init__(con_str)
        self.url = url

    def parse_worker(self):

        """ Создадим воркера который будет парсить страницу один раз в указанное время """

        while True:
            db = self.connect_to_db('py_test_db')
            db.py_test.remove({}) # очистим данные в бд в начале каждого шага воркера, как я понял данные должны постоянно обновляться судя по тз, возможно ошибся, если другое требование переделаю согласно нему.
            db.counters.remove({})

            res = requests.get(self.url)

            html_content = BeautifulSoup(res.content, 'html.parser')
            output = html_content.find_all('a', class_='storylink') # вытаскиваем все что соответствует классу, так как только нужные нам элементы на странице имеют такой класс

            logging.info(output)

            for content in output: # заливаем данные в бд, из за требований к индексу пришлось обойтись без insert_many
                db.py_test.insert({"_id": self.get_next_id('py_test_db', "py_test"),
                                   "title": content.get_text(),
                                   'url': content.get('href'),
                                   'created': datetime.now().isoformat()
                                   })

            time.sleep(3600) # время, можно будет перенести в кофиг файл
