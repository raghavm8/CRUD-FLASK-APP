from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configurations.config import Config
from routes import todo_bp
from routes import auth_bp
from routes import main_bp
from models import db
from configurations.login_config import login_manager
from models import User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(todo_bp)
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
