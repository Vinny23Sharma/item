import sqlite3
from flask_restful import Resource, reqparse
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(self, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))# It has to be in the form of a tuple
        row = result.fetchone() # We will get first row after the result select_query
        if row:
            user = User(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
      type=str,
      required=True,
      help="This field cannot be blank."
    )
    parser.add_argument('password',
      type = str,
      required=True,
      help="This field cannot be blank."
    )

    def post(self):

        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "A user with that username already exists."}, 400
            

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)" # id is auto incrementing so we have to insert NULL
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."},201
