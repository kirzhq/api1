# http://127.0.0.1:5000/hi http://127.0.0.1:5000/hi/ http://127.0.0.1:5000/hi/2

from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

list = [
     {
          "id": 1,
          "text": "Привет Мир",
          "lang": "RU"
     },
     {
          "id": 2,
          "text": "Hello world!",
          "lang": "EN"
     },
     {
          "id": 3,
          "text": "Hello die Welt!!",
          "lang": "DE"
     },
     {
          "id": 4,
          "text": "こんにちは。",
          "lang": "JP"
     }
]

class HiResource(Resource):
     def get(self, id = 0):
          if id == 0:
               return random.choice(list), 200
          for value in list:
               if(list["id"] == id):
                    return value, 200
          return "Error! This request can't be completed", 404
     

if __name__ == '__main__':
     app = Flask(__name__)
     api = Api(app)
     api.add_resource(HiResource, "/hi", "/hi/", "/hi/<int:id>")
     app.run(debug = True)
