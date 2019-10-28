class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/yourdatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'change more secure'
    JWT_SECRET_KEY = 'change more secure'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'your database'
    MYSQL_DATABASE_HOST = 'localhost'
    JSON_SORT_KEYS = False