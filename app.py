from flask import Flask
from configurations.config import Config
from models.todoModel import db
from routes import todo_bp 

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(todo_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
