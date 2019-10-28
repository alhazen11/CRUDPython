from app import app, entities, jwt
from app.resources import Token, User
from flask_restful import Api
api = Api(app)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedToken.is_jti_blacklisted(jti)

api.add_resource(Token.Index, '/')

