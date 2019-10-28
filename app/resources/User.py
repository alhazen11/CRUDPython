from app import app
from flask_restful import Resource, reqparse
from app import bcrypt
from app.models.User import User

registParser = reqparse.RequestParser()
registParser.add_argument('name', help = 'This field cannot be blank', required = True)
registParser.add_argument('city', help = 'This field cannot be blank', required = True)
registParser.add_argument('email', help = 'This field cannot be blank', required = True)
registParser.add_argument('password', help = 'This field cannot be blank', required = True)

class ApiUsers(Resource):
    def post(self):
        data = registParser.parse_args()

        if User.find_by_email(data['email']):
          return {'message': 'User email {} already exists'. format(data['email'])}

        new_user = User(
            name = data['name'],
            email = data['email'],
            password = bcrypt.generate_password_hash(data['password']).decode('utf-8'),
            city = data['city']
        )
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['email'])
            refresh_token = create_refresh_token(identity = data['email'])
            return {
                'message': 'User email {} created'.format( data['email']),
                'access_token': access_token,
                'refresh_token': refresh_token,
            }
        except:
            return {'message': 'Something went wrong.'}, 500

    def get(self):
        return User.return_all()