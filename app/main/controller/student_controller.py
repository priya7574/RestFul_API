# print("Student_controller")
from flask import request
from flask_restplus import Resource
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

from app.configration import SECRET_KEY

from ..util.dto import StudentDto
from ..service.student_service import save_new_student, get_all_students, get_a_student
import jwt

api = StudentDto.api
_student = StudentDto.student


@api.route('/')
class StudentList(Resource):
    @api.doc('list_of_registered_students')
    @api.marshal_list_with(_student, envelope='data')
    def get(self):
        """List all registered students"""
        return get_all_students()

    @api.response(201, 'student successfully created.')
    @api.doc('create a new student')
    @api.expect(_student, validate=True)
    def post(self):
        """Creates a new student """
        data = request.json
        return save_new_student(data=data)


@api.route('/<token>')
@api.param('token', 'token')
@api.response(404, 'student not found.')
class Student(Resource):
    @api.doc('get a student')
    @api.marshal_with(_student)
    def get(self, token):
        '''get a student given its identifier'''
        student = get_a_student(token)
        # email_token = jwt.decode({'key': email}, SECRET_KEY, algorithm='HS256')
        # print("..........................................",email_token)
        if not token:
            api.abort(404)
        else:
            return student



class SecretResource(Resource):
    @api.doc('secret')
    def get(self):
        return {
            'answer': 42
        }
