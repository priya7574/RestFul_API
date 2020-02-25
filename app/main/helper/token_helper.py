from flask import request, abort, make_response
from functools import wraps
from app.configration import SECRET_KEY
import jwt

JSON_MIME_TYPE = 'application/json'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        headers = request.headers
        token = None
        try:
            if headers.get('Authorization'):
                token = headers.get('Authorization').split('Bearer ')[1]
            else:
                url = str(request)
                token = url.split('?token=')[1].split("'")[0]
        except Exception as exe:
            return False

        response = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if response.get('key') == 'my_token':
            pass
        else:
            abort(401, 'token is incorrect')
        return f(*args, **kwargs)
    return decorated
