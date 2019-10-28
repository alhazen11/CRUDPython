from app import app, entities, jwt
from app.resources import Token, User
from flask_restful import Api
api = Api(app)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedToken.is_jti_blacklisted(jti)

api.add_resource(Token.Index, '/')
api.add_resource(User.ApiUsers, '/api/users') # POST: Regist User, GET: Get All Users
api.add_resource(User.ApiUsersID, '/api/users/<int:id>') # DELETE: Delete User by ID, GET: Get User by ID, PUT: Update user by ID
api.add_resource(User.ApiLogin, '/api/login') # POST: Login
api.add_resource(User.UserLogoutAccess, '/api/logout/access')
api.add_resource(User.UserLogoutRefresh, '/api/logout/refresh')
api.add_resource(Token.TokenRefresh, '/api/token/refresh')

