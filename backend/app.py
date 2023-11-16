from flask import Flask, request, jsonify
from db import DataBase
from bson import json_util
import json

app = Flask(__name__)

db = DataBase()
db.init_db()


@app.route('/', methods=['GET'])
def get_form():
    data = db.get_data()
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
