
















# import sys, gzip, json
# from chalice import Chalice,Request
# app = Chalice(app_name='app_test_1')

# in_put = {
#     "user": [
#         {
#             "name": "hungmanh",
#             "age": 25,
#             "address": "hai duong"
#         },
#         {
#             "name": "trang",
#             "age": 25,
#             "address": "ha noi"
#         },
#         {
#             "name": "linh",
#             "age": 25,
#             "address": "hcm"
#         },
#         {
#             "name": "hoa",
#             "age": 25,
#             "address": "da nang"
#         }
#     ]
# }

# out_put ={
    
# }
# @app.route('/{user_name}', methods= ['GET'])
# def get_users(user_name):
#     for item in in_put["user"]:
#         if user_name == item["name"]:
#             return item

# @app.route('/', methods= ['POST' ,'PUT'])



# @app.route('/delete/id={use_id}', methods= ['DELETE'])









# import sys, gzip, json
# from chalice import Chalice,Response
# from chalice import BadRequestError
# from chalice import NotFoundError
# from urllib.parse import urlparse, parse_qs


# app = Chalice(app_name='app_test_1')
# app.debug = True
# in_put = {
#     "user": [
#         {
#             "name": "hungmanh",
#             "age": 25,
#             "address": "hai duong"
#         },
#         {
#             "name": "trang",
#             "age": 25,
#             "address": "ha noi"
#         },
#         {
#             "name": "linh",
#             "age": 25,
#             "address": "hcm"
#         },
#         {
#             "name": "hoa",
#             "age": 25,
#             "address": "da nang"
#         }
#     ]
# }



# out_put ={
    
# }
# @app.route('/{user_name}', methods= ['GET'])
# def get_users(user_name):
#     for item in in_put["user"]:
#         if user_name == item["name"]:
#             out_put["user"] = item
#             return out_put
#         else: {"error : not found"}

# @app.route('/put', methods = ['PUT'])
# def put_users():
#     return app.current_request.to_dict()
# @app.route('/' , methods = ['POST'], 
#            content_types = ['application/x-www-form-urlencoded'])

# def index():
#     parsed = parse_qs(app.current_request.raw_body.decode())
#     return {
#         'states' : parsed.get('state' ,[])
#     }

# @app.route('/')
# def index():
#     return Response(body = 'hello world!',
#                     status_code = 200,
#                     headers = {'Content-Type': 'text/plain'})


# @app.route('/cities/{citi}')
# def state_of_citi(citi):
#     try:
#         return {'state' : CITIES_TO_STATE[citi]}
#     except KeyError:
#         raise BadRequestError("Unknow citi '%s', valid choices are: %s" %(citi,', '.join(CITIES_TO_STATE.keys())))

# @app.route('/resource/{value}', methods = ['PUT'])
# def put_test(value):
#     return {"value": value}
# OBJ = {
#     "mykey" : {
#         "foo" : "bar"
#     }
    
# }
# @app.route('/myobj/{key}' , methods = ['PUT', 'GET'])
# def myobj(key):
#     request = app.current_request
#     if request.method == 'PUT':
#         OBJ[key] = request.json_body
#     elif request.method == 'GET':
#         try:
#             return {key: OBJ[key]}
#         except KeyError:
#             raise NotFoundError(key)

# @app.route('/introspect')
# def introspect():
#     return app.current_request.to_dict()



# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#