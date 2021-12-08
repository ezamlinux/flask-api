from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('users', description='users related operations')
    user = api.model('User', {
        'id': fields.Integer(),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
    })
