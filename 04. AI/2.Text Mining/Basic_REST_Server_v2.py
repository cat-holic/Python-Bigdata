from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.debug = True
api = Api(app)


class CreateUser(Resource):
    def get(self):
        return {'status': 'cu1 success'}


api.add_resource(CreateUser, '/user')


class CreateUser2(Resource):
    def get(self):
        return {'status': 'cu2 success'}


api.add_resource(CreateUser2, "/user2")


class Multi(Resource):
    def get(self, num):
        return {'result': num * 10}


api.add_resource(Multi, '/multi/<int:num>')
if __name__ == "__main__":
    app.run(host='192.168.0.35')
