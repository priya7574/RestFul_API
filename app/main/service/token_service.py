import datetime
from ...configration import SECRET_KEY
import uuid
import jwt


def create_token():
    response = {}
    code = None
    try:
        token = jwt.encode({'key': 'my_token'}, SECRET_KEY, algorithm='HS256')
        response['token'] = token.decode("utf-8")
        response['success'] = True
        code = 201
    except Exception as exp:
        response['error'] = True
        response['token'] = None
        code = 400
    return response, code
