from flask import request
from flask_restplus import Resource
from ..util.dto import UserDto
from ..helper.token_helper import token_required
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
@api.param('token', 'Access Token', required=True)
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    @token_required
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    @token_required
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.param('token', 'Access Token', required=True)
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    @token_required
    def get(self, etoken):
        """get a user given its identifier"""
        user = get_a_user(etoken)
        if not user:
            api.abort(404)
        else:
            return user
