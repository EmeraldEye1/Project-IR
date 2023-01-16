import bcrypt
from sqlalchemy import event

from .bookmark import Bookmark
from .user import User
from .database import db


@event.listens_for(User.__table__, 'after_create')
def create_user(*args, **kwargs):
    db.session.add(
        User(username='tan', password=bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt(10)),
             email='tan@hotmail.com'))
    db.session.add(
        User(username='smart', password=bcrypt.hashpw('5678'.encode('utf-8'), bcrypt.gensalt(10)),
             email='smart@hotmail.com')),
    db.session.commit()


# @event.listens_for(Bookmark.__table__, 'after_create')
# def create_bookmark(*args, **kwargs):
#     db.session.add(Bookmark(uid='1', ani_id='1'))
#     db.session.commit()