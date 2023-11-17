from flask import Flask, request, jsonify
from bson import json_util
import json

from db import DataBase
from validate import get_type_data


app = Flask(__name__)

db = DataBase()
db.init_db()



@app.route('/', methods=['GET'])
def get_data():
    data = db.get_data()
    return data

@app.route('/get_form', methods=['POST'])
def get_form():

    out_data = dict()
    user_data = dict(request.args)

    for key, value in user_data.items():
        type_value = get_type_data(value)
        out_data.update({key:type_value})


    return out_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
