import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:raghav@localhost:3306/Todo"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)