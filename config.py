import os

# configure our database
DATABASE = {
    'name': 'chinook.db',
    'engine': 'peewee.SqliteDatabase',
}
DATABASE_URL = 'sqlite:///chinook.db'
DEBUG = True
SECRET_KEY = os.urandom(24) # 'ssshhhh'
PORT = 8080

# Other configuration options as needed
LOGGING_LEVEL = 'INFO'
SESSION_COOKIE_NAME = 'flask_app_session'