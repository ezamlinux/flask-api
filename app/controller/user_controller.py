from flask import request
from flask_restx import Resource

from ..util.user_dto import UserDto
from ..service.user_service import *

ns_user = UserDto.api
_user = UserDto.user

@ns_user.route('/')
class UserList(Resource):

    @ns_user.doc('list_of_registered_users')
    @ns_user.marshal_with(_user, as_list=True)
    def get(self):
        """List all registered users"""

        return get_all()

    @ns_user.doc('create a new user')
    @ns_user.expect(_user, validate=True)
    @ns_user.marshal_with(_user)
    @ns_user.response(201, 'User successfully created.')
    def post(self):
        """Creates a new User"""

        return save(request.json)

##################################
# Resource access / modification #
##################################

@ns_user.route('/<int:user_id>')
@ns_user.param('user_id', 'The User identifier')
@ns_user.response(404, 'User not found.')
class User(Resource):

    @ns_user.doc('get a user')
    @ns_user.marshal_with(_user)
    def get(self, user_id):
        """get a user given its identifier"""
        user = get(user_id)
        if not user:
            ns_user.abort(404, message="User not Found")
        else:
            return user

    @ns_user.doc('modify a user')
    @ns_user.expect(_user, validate=True)
    @ns_user.marshal_with(_user)
    @ns_user.response(200, 'User successfully modified.')
    def put(self, user_id):
        """modify a user given its identifier"""

        return modify(user_id, request.json)

    @ns_user.doc('delete a user')
    @ns_user.response(200, 'User successfully deleted.')
    def delete(self, user_id):
        """delete a user given its identifier"""

        return delete(user_id)
