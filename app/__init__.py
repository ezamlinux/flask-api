from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ERROR_404_HELP'] = False # A commenter si on veut "You have requested this URI [/users/1] but did you mean /users/<int:user_id> ?"
db = SQLAlchemy(app)
db.create_all()

# ROOT API
root_api = Api(app)
# remove default namespace
root_api.namespaces.clear()

# Register Routes
from app.controller.user_controller import UserList, User, ns_user

# USER API
root_api.add_namespace(ns_user)
root_api.add_resource(UserList)
root_api.add_resource(User)
