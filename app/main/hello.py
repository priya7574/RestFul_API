import jwt
#
# def create_token(email):
#     response = {}
#     code = None
#     try:
#         token = jwt.encode({'key': 'email'}, SECRET_KEY, algorithm='HS256')
#         print(token)
#         print(type(token))
#         #response['token'] = token.decode("utf-8")
#         #response['success'] = True
#     except Exception as exp:
#         response['error'] = True
#         response['token'] = None
#         code = 400
#     return response, code
email=input("enter :")
SECRET_KEY = 'vhnjsdgfsuydiwmnsd56775ajslkaj'
token = jwt.encode({'key': email}, SECRET_KEY, algorithm='HS256')
print(token)
print(type(token))
detoken = jwt.decode(token, SECRET_KEY, algorithm='HS256')
print(type(detoken))
print(detoken)


response = jwt.decode(token, secret, algorithms=['HS256'])
        if response.get('key') == 'my_token':
            pass
        else:
            abort(401, 'token is incorrect')
        return f(*args, **kwargs)