from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .todo_model import Todo
from .user_model import User