from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Todo
from .db import db

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('base.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ユーザー認証
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.todo_list'))
        flash('Invalid username or password')
        return redirect(url_for('main.login'))
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ユーザー登録
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('main.register'))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('main.login'))

    return render_template('register.html')

# ToDoリストページ
@main.route('/todos')
@login_required
def todo_list():
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template('todo_list.html', todos=todos)

# ToDo詳細ページ
@main.route('/todos/<int:todo_id>')
@login_required
def todo_detail(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if not todo:
        return "ToDo not found", 404
    return render_template('todo_detail.html', todo=todo)

# ToDo追加
@main.route('/add_todo', methods=['POST'])
@login_required
def add_todo():
    new_todo = Todo(
        user_id=current_user.id,
        todo_text=request.form['todo_text'],
        description=request.form['description']
        )
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main.todo_list'))

# 編集フォームの表示
@main.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)  # 指定されたIDのToDoを取得

    if request.method == 'POST':
        # フォームから送信されたデータでToDoを更新
        todo.todo_text = request.form['todo_text']

        # 変更を保存
        db.session.commit()

        flash('ToDo updated successfully!', 'success')  # フラッシュメッセージ
        return redirect(url_for('main.todo_list'))

    # GETリクエストの場合、編集フォームを表示
    return render_template('todo_edit.html', todo=todo)