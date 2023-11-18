from pymongo import MongoClient
import os

from db.inition import data


class DataBase:
    def __init__(self) -> None:
        """получаем курсор к базе данных"""
        # получаем ссылку для поключения
        url = self.__get_url()

        client = MongoClient(url)
        db = client.form_templates
        self.conn = db.templates


    def init_db(self):
        """заполняем данными если пустая база данных"""
        if self.conn.count_documents({}) == 0:
            self.conn.insert_many(data)


    def get_cursor (self):
        """получение collection"""
        return self.conn.find()


    def __get_url(self) -> str:
            """создаем ссылку для подключения"""
            host = os.environ['HOST']
            user = os.environ['USER']
            password = os.environ['PASSWORD']
            port = os.environ['PORT']

            return 'mongodb://' + user + ':' + password +\
                '@' + host + ':' + port