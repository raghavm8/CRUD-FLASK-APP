from flask import Blueprint, render_template, request, redirect
from flask_login import login_required
from models import db, Todo
from flask_login import current_user

# Create blueprint
todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/')
@login_required
def read_todo():
    all = Todo.query.all()
    return render_template('index.html')

@todo_bp.route('/todos')
@login_required
def read_todo_list():
    all = Todo.query.filter_by(created_by=current_user.id).all()
    return render_template('todos.html', allTodo=all)

@todo_bp.route('/allUsers/Manager/todos/<int:created_by_id>')
@login_required
def read_todo_list_per_user(created_by_id):
    all = Todo.query.filter_by(created_by=created_by_id).all()
    return render_template('todos.html', allTodo=all)

@todo_bp.route('/add', methods=['POST'])
@login_required
def add_todo():
    title = request.form['title']
    description = request.form['description']
    created_by = current_user.id
    todo = Todo(title=title, description=description, created_by=created_by)
    db.session.add(todo)
    db.session.commit()
    return redirect('/todos')

@todo_bp.route('/edit/<int:id>')
@login_required
def edit_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    return render_template('update.html', todo=todo)

@todo_bp.route('/update/<int:id>', methods=['POST'])
@login_required
def edit_todo_save(id):
    title = request.form['title']
    description = request.form['description']
    todo = Todo.query.filter_by(id=id).first()
    todo.title = title
    todo.description = description
    db.session.commit()
    return redirect('/')

@todo_bp.route('/delete/<int:id>')
@login_required
def delete_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')
