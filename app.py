from flask import Flask
from flask_restful import Api, Resource
from flask_jwt import JWT
from security import identity, authenticate
from db import db

from resources.user import UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'miguel'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World'}


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(HelloWorld, '/hello')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
