from flask import Blueprint, render_template, request, redirect
from models import db, Todo

# Create blueprint
todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/')
def read_todo():
    all = Todo.query.all()
    return render_template('index.html', allTodo=all)

@todo_bp.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    description = request.form['description']
    todo = Todo(title=title, description=description)
    db.session.add(todo)
    db.session.commit()
    return redirect('/')

@todo_bp.route('/edit/<int:id>')
def edit_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    return render_template('update.html', todo=todo)

@todo_bp.route('/update/<int:id>', methods=['POST'])
def edit_todo_save(id):
    title = request.form['title']
    description = request.form['description']
    todo = Todo.query.filter_by(id=id).first()
    todo.title = title
    todo.description = description
    db.session.commit()
    return redirect('/')

@todo_bp.route('/delete/<int:id>')
def delete_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')
