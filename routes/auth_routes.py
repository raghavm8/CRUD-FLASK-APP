from flask import Blueprint, render_template, redirect, url_for
from flask import request
from flask import flash
from models import db
from models import User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required


auth_bp = Blueprint('auth','__name__')

@auth_bp.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@auth_bp.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@auth_bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, password):
        flash("Wrong credentials")
        return redirect(url_for('auth.login'))
    
    login_user(user)
    return redirect(url_for('todo.read_todo'))

@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    if user:
        flash("Email already exists.")
        return redirect(url_for('auth.login'))
    
    new_user = User(email=email, name=name, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.profile'))