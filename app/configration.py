

SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
import jwt
response={}
token = jwt.encode({'key': 'hello'}, SECRET_KEY, algorithm='HS256')
response['token'] = token.decode("utf-8")
print(response['token'])
# newtoken = jwt.decode({'key': token}, SECRET_KEY, algorithm='HS256')
# response['newtoken'] = newtoken.decode("utf-8")
# print(newresponse)
'''        response['success'] = True
        code = 201
    except Exception as exp:
        response['error'] = True
        response['token'] = None
        code = 400
    return response, code
response={}
    code=None
    try:token = jwt.decode({'key': email}, SECRET_KEY, algorithm='HS256')
        response['token'] = token.decode("utf-8")
        response['success'] = True
        code = 300


    except Exception as exp:
        response['error'] = True
        response['token'] = None
        code=600
    return response, code'''