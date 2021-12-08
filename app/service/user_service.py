from app.model.user_model import User
from app import db

def get(user_id):
    return User.query.get(user_id)

def get_all():
    return User.query.all()

def save(data):
    user = User(username= data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return user

def modify(user_id, data):
    user = db.session.query(User).get(user_id)
    user.username = data['username']
    user.email = data['email']
    db.session.commit()
    return user

def delete(user_id):
    db.session.query(User).filter(User.id==user_id).delete()
    db.session.commit()
    return True

