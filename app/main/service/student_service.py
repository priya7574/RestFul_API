# print("student_service")
import uuid
import datetime
# from ..helper.token import create_token
# from ..helper.token import decode_token
from app.main import db
from app.main.model.student import Student
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)


def save_new_student(data):
    pass
'''
    print(data)
    global token
    student = Student.query.filter_by(email=data['email']).first()
    if not student:
        new_student = Student(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            studentname=data['studentname'],
            password=data['password'],
            department=data['department'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_student)
        email = data.get('email')
        # if id:
        access_token = create_token(email)
        print(access_token)
        if access_token[1] == 201:
            token = access_token[0]['token']
            print(',.,.,.,.,.,,')
            response_object = {
                'status': 'success',
                # 'message': 'Successfully registered.',
                'message': 'Student {} was created'.format(data['studentname']),
                'access_token': token
            }
            return response_object, 201


    else:
        response_object = {
            'status': 'Failed',
            'message': 'Existing Student ',
            # 'message': 'User {} was created'.format(data['username']),
            # 'access_token': access_token,
            # 'refresh_token': refresh_token
        }
        return response_object, 500

'''


def get_all_students():
    return Student.query.all()


def get_a_student(token):
    # check_email=decode_token(etoken)
    # print(check_email)
    return Student.query.filter_by(token=token).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
# '''