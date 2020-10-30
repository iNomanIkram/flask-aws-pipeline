from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return {'msg':'hello world'},200

api.add_resource(Test,'/')
app.run()