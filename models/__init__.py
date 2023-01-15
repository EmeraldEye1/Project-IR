import bcrypt
from sqlalchemy import event
from .user import User
from .database import db


@event.listens_for(User.__table__, 'after_create')
def create_user(*args, **kwargs):
    db.session.add(
        User(username='tan', password=bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt(10)),
             email='tan@hotmail.com',
             bookmark=None, favorite=None))
    db.session.commit()
    db.session.add(
        User(username='Poom', password=bcrypt.hashpw('5678'.encode('utf-8'), bcrypt.gensalt(10)),
             email='poom007@hotmail.com')),
    db.session.commit()