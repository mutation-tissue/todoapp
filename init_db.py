from app import create_app, db
from app.models import User  # 必要に応じて他のモデルをインポート

# flask db init
# flask db migrate
# flask db upgrade

# アプリケーションを作成
app = create_app()

# アプリケーションコンテキストを使用
with app.app_context():
    try:
        # 必要に応じてデータを追加
        if not User.query.filter_by(username='admin').first():
            print("Adding default user...")
            admin_user = User(username='admin')
            admin_user.set_password('admin')  # パスワードをハッシュ化
            db.session.add(admin_user)
            db.session.commit()
            print("Default user added successfully!")
        else:
            print("Default user already exists.")

        if not User.query.filter_by(username='user').first():
            print("Adding default user...")
            admin_user = User(username='user')
            admin_user.set_password('user')  # パスワードをハッシュ化
            db.session.add(admin_user)
            db.session.commit()
            print("Default user added successfully!")
        else:
            print("Default user already exists.")
        print("Database initialization complete!")
    except Exception as e:
        print(f"An error occurred: {e}")
