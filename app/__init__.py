from flask import Flask
from flask_login import LoginManager
from .models import User
from .db import db
from config import Config

login_manager = LoginManager()

def create_app():
    app = Flask(__name__, static_folder='static')
    #app.config['SECRET_KEY'] = 'your_secret_key'
    app.config.from_object(Config)  # config.py を読み込む
    db.init_app(app)

    login_manager.init_app(app)

    # ログインが必要なページへのリダイレクト先を指定
    login_manager.login_view = 'main.login'

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from .routes import main  # ルートのブループリントを登録
    app.register_blueprint(main)


    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))