from pymongo import MongoClient
import os

from bson import json_util
import json

from db.inition import data


class DataBase:
    def __init__(self) -> None:
        """получаем курсор к базе данных"""
        # получаем ссылку для поключения
        # url = self.__get_url()
        url = 'mongodb://localhost:27017'

        client = MongoClient(url)
        db = client.form_templates
        self.conn = db.templates


    def get_data(self):
        data = self.conn.find_one({'name':'OrderForm'})
        return self.__bson_to_json(data)


    def init_db(self):
        """заполняем данными если пустая база данных"""
        if self.conn.count_documents({}) == 0:
            self.conn.insert_many(data)


    def __get_url(self) -> str:
            """создаем ссылку для подключения"""
            host = os.environ['HOST']
            user = os.environ['USER']
            password = os.environ['PASSWORD']
            port = os.environ['PORT']

            return 'mongodb://' + user + ':' + password +\
                '@' + host + ':' + port
        
    
    def __bson_to_json(self, data) -> json:
        return json.loads(json_util.dumps(data))