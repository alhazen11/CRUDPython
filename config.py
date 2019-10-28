class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/crudpython'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'crudpythoncrudpython'
    JWT_SECRET_KEY = 'crudpythoncrudpython'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'crudpython'
    MYSQL_DATABASE_HOST = 'localhost'
    JSON_SORT_KEYS = False