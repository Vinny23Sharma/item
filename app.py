from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app) # create Api and we can add resources to our Api

jwt = JWT(app, authenticate, identity) #/auth a new end point  will create a new endpoint
# When we call the auth endpoint. It will send the username and password to authenticate method and then the authenticate method send the jwt token to the identity where the jwtpayload provides us with correct code.
 # If it can doo that it means that the JWT_token is authentic


# adding the resources to the api
api.add_resource(Item,'/item/<string:name>' ) #http://127.0.0.1:5000/Student
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
# Because we do not want to run the file if we have imported it.

app.run(port = 5000, debug=True)
