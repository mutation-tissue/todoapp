import os
import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)
    # データベースURIのフォーマット: dialect+driver://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/todoapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 不要なメモリ消費を防ぐ


    
