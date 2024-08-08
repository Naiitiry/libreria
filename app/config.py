import os
from dotenv import load_dotenv

class Configuration():
    load_dotenv()
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('FULL_URI')
    SQLALCHEMY_TRACK_MODIFICATIN = False
