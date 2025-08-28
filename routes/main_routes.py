from flask import Blueprint, render_template
from flask_login import login_required

main_bp = Blueprint('main', '__name__')

@main_bp.route('/auth_index')
@login_required
def auth_index():
    return "retuned page"

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html') 