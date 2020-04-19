from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='You need to specify a username'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='You need to specify a password'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {
                    'message': "username '{}' is already taken."
                    .format(data['username'])
                    }, 400

        user = UserModel(**data)

        user.save_to_db()

        return {'message': 'User created succesfully'}, 201
