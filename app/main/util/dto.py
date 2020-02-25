from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='users related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class StudentDto:
    api = Namespace('student', description='student related operations')
    student = api.model('student', {
        'email': fields.String(required=True, description='stduent email address'),
        'studentname': fields.String(required=True, description='student username'),
        'password': fields.String(required=True, description='student password'),
        'public_id': fields.String(description='The Student Identifier'),
        'department': fields.String(description='Department Identifier')
    })


class TokenDto:
    api = Namespace('Token', description='Generate Token')
