from flask import Blueprint, render_template, redirect, url_for
from flask import request
from flask import flash
from models import db
from models import User
from flask_login import login_required
from models.Enums.role_enum import Role

user_bp = Blueprint('user','__name__')

@user_bp.route('/allUsers/Admin')
@login_required
def read_users_list():
    all_users = User.query.filter_by(role=Role.USER).all()
    return render_template('UsersDashboardForAdmin.html', users = all_users)

@user_bp.route('/allManagers/Admin')
@login_required
def read_manager_list():
    all_managers = User.query.filter_by(role=Role.MANAGER).all()
    return render_template('ManagersDashboardForAdmin.html', managers = all_managers)


@user_bp.route('/allUsers/makemanager/<int:id>')
@login_required
def make_manager(id):
    user = User.query.filter_by(id = id).first()
    user.role = Role.MANAGER
    db.session.commit()
    return redirect('/allUsers/Admin')
    
    
@user_bp.route('/makeuser/<int:id>')
@login_required
def make_user(id):
    user = User.query.filter_by(id = id).first()
    user.role = Role.USER
    db.session.commit()
    return redirect('/allManagers/Admin')

@user_bp.route('/userupdate/<int:id>', methods=['GET'])
def edit_user_save(id):
    user = User.query.filter_by(id=id).first()
    user.role = Role.ADMIN
    db.session.commit()
    return redirect('/')
       
@user_bp.route('/allUsers/Manager/<int:id>')
@login_required
def read_user_list_per_manager(id):
    all = User.query.filter_by(manager_id=id).all()
    return render_template('UsersDashboardForManager.html', allUser=all)