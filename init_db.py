from app import create_app, db
from app.models import User  # 必要に応じてモデルをインポート

# アプリケーションを作成
app = create_app()

# アプリケーションコンテキストを使用
with app.app_context():
    # データベースを初期化
    print("Initializing database...")
    db.create_all()  # テーブルを作成

    # 必要に応じてデータを追加
    if not User.query.filter_by(username='admin').first():
        print("Adding default user...")
        admin_user = User(username='admin')
        admin_user.set_password('admin')  # パスワードをハッシュ化
        db.session.add(admin_user)
        db.session.commit()
    print("Database initialization complete!")
