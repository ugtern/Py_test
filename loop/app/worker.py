import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from app.databases import MongoDB


class WorkerClass(MongoDB):
    def __init__(self, con_str, url):
        super().__init__(con_str)
        self.url = url

    def parse_worker(self):
        while True:
            db = self.connect_to_db('py_test_db')
            db.py_test.remove({})
            db.counters.remove({})

            res = requests.get(self.url)

            html_content = BeautifulSoup(res.content, 'html.parser')
            output = html_content.find_all('a', class_='storylink')

            for content in output:
                db.py_test.insert({"_id": self.get_next_id('py_test_db', "py_test"),
                                   "title": content.get_text(),
                                   'url': content.get('href'),
                                   'created': datetime.now().isoformat()
                                   })

            time.sleep(3600)
