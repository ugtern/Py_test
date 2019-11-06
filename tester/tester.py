import requests
import json
import logging

""" 
Тестер служит исключительно для проверки методов api, 
используя библиотеку requests отправим тестовые запросы к нашему api
"""


class Tester:

    logging.basicConfig(filename='tester_log.log', level=logging.DEBUG)

    def __init__(self):
        with open('tester_config.json') as file:
            file = json.load(file)
        self.url = file['url']

    def test_get(self):
        res = requests.get(self.url)
        logging.info(res.text)

    def test_get_sort(self, col):
        res = requests.get('{}?order={}'.format(self.url, col))
        logging.info(res.text)

    def test_get_limit(self, value):
        res = requests.get('{}?limit={}'.format(self.url, value))
        logging.info(res.text)

    def test_get_offset(self, value):
        res = requests.get('{}?offset={}'.format(self.url, value))
        logging.info(res.text)

    def test_get_all_params(self, params):
        res = requests.get('{}?order={}&offset={}&limit={}'.format(self.url, params[0], params[1], params[2]))
        logging.info(res.text)


test = Tester()
test.test_get()
test.test_get_sort('title')
test.test_get_offset(15)
test.test_get_limit(2)
test.test_get_all_params(['title', 5, 15])

