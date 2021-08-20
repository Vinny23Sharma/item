from flask import Flask
from flask_restful import Api
from resources.user import User
from resources.user_personal_info import User_personal_info
from resources.user_contact_info import User_contact_info
from resources.user_educational_info import User_educational_info

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/user')
api.add_resource(User_personal_info, '/user/personal_info/<string:username>')
api.add_resource(User_educational_info, '/user/educational_info/<string:username>')
api.add_resource(User_contact_info, '/user/contact_info/<string:username>')

app.run(port=5000, debug=True)
