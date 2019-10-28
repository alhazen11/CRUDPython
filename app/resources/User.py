from app import app
from flask_restful import Resource, reqparse
from app import bcrypt
from app.models.User import User

registParser = reqparse.RequestParser()
registParser.add_argument('name', help = 'This field cannot be blank', required = True)
registParser.add_argument('city', help = 'This field cannot be blank', required = True)
registParser.add_argument('email', help = 'This field cannot be blank', required = True)
registParser.add_argument('password', help = 'This field cannot be blank', required = True)

loginParser = reqparse.RequestParser()
loginParser.add_argument('email', help = 'This field cannot be blank', required = True)
loginParser.add_argument('password', help = 'This field cannot be blank', required = True)

editParser = reqparse.RequestParser()
editParser.add_argument('parent_id')
editParser.add_argument('name')
editParser.add_argument('city')
editParser.add_argument('email')
editParser.add_argument('password')
editParser.add_argument('notification')
editParser.add_argument('auto_ml')

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

class ApiUsersID(Resource):
    def get(self, id):
        return User.find_by_id(id)

    def delete(self, id):
        return User.delete(id)

    def put(self, id):
        data = editParser.parse_args()
        parent_id = data['parent_id']
        name = data['name']
        email = data['email']
        password = ''
        notification = data['notification']
        auto_ml = data['auto_ml']
        city = data['city']
        return User.update(id, parent_id, name, email, password, notification, auto_ml, city)


class ApiLogin(Resource):
    def post(self):
        data = loginParser.parse_args()
        current_user = User.find_by_email(data['email'])
        if not current_user:
            return {'message': 'User email {} doesn\'t exist'.format(data['email'])}
        
        if bcrypt.check_password_hash(current_user.password, data['password']):
            access_token = create_access_token(identity = data['email'])
            refresh_token = create_refresh_token(identity = data['email'])
            return {
                'message': 'Logged in as {}'.format(current_user.email),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong credentials'}