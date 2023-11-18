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


    def find_matching_template(self, data) -> str | None:
        """поиск нужной формы"""
        cursor = self.conn.find()

        for document in cursor:
            #получаем ключи формы и удаляем ненужные
            template_fields = set(document.keys()) - {'name'} - {'_id'} 
            print("TEMPLATE",template_fields)
            
            data_fields = set(data.keys())
            print("DATA",data_fields)

            #проверяем на одинаковые ключи
            if data_fields.issuperset(template_fields):
                print("GOGOGO")
                # проверяем на одинаковое значение
                valid = all(self.__check_value(document[field], data[field]) for field in template_fields)
                if valid:
                    return document['name']
        return None
        

    def __check_value(self, template, data) -> bool:
        if template == data:
            return True
        


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