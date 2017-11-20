import datetime
from app import db

class User(db.Document):
    username = db.StringField(unique=True)
    password = db.StringField(default=True)
    active = db.BooleanField(default=True)
    isAdmin = db.BooleanField(default=False)
    key = db.StringField(default=False)
    timestamp = db.DateTimeField(default=datetime.datetime.now())
