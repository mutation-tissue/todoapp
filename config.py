import os
import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
