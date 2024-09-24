# Description: This file contains the API endpoints for the application. The API endpoints are used to create, read, update and delete users and data. The API endpoints are implemented using the Flask-RESTful library. The API endpoints are implemented as classes that inherit from the Resource class. The API endpoints are registered with the Flask application using the Api class. The API endpoints are implemented using the marshal_with decorator to serialize the response data. The API endpoints are implemented using the reqparse module to parse the request data. The API endpoints are implemented using the abort function to return error responses. The API endpoints are implemented using the User and Data models to interact with the database. The API endpoints are implemented using the bcrypt module to hash the user passwords.
from flask_restful import Resource, Api, marshal_with, fields, reqparse, abort
from tracker.model import User, Data
from flask_bcrypt import Bcrypt

# Create an instance of the Api class
bcrypt = Bcrypt()

# Define the fields for the response data for the user
user_fields = {
        'id': fields.Integer,
        'firstname': fields.String,
        'lastname': fields.String,
        'email': fields.String
    }

# Define the fields for the response data for the data
data_fields = {
            'id': fields.Integer,
            'systolic': fields.Integer,
            'diastolic': fields.Integer,
            'pulse': fields.Integer,
            'user_id': fields.Integer
        }

# Create the UsersResource class
class UsersResource(Resource):
    def __init__(self):
        # The __init__ method is used to initialize the UsersResource class. It is used to create an instance of the reqparse.RequestParser class and add the required arguments to the parser.
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('firstname', type=str, required=True, help='First name is required')
        self.parser.add_argument('lastname', type=str, required=True, help='Last name is required')
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')
  

    @marshal_with(user_fields)
    def post(self):
        # The post method is used to create a new user. It is used to parse the request data using the reqparse module. It is used to check if a user with the same email already exists. It is used to create a new user object and add it to the database. It is used to commit the changes to the database. It is used to return the new user object and the status code 201.
        from tracker import db
        # The args variable is used to parse the request data using the reqparse module.
        args = self.parser.parse_args()
        # Get the user with the same email from the database
        user = User.query.filter_by(email=args['email']).first()
        if user:
            # Abort if the user with the same email already exists
            abort(409, message=f'User with email {args["email"]} already exists.')
        # Create a new user object
        user = User(firstname=args['firstname'], lastname=args['lastname'], email=args['email'], password_hash=args['password'])
        db.session.add(user)
        db.session.commit()
        return user, 201
      
    @marshal_with(user_fields)
    def get(self):
        # The get method is used to get all the users. It is used to query all the users from the database. It is used to return the list of users and the status code 200.
        users = User.query.all()
        return users, 200


# Create the UserResource class   
class UserResource(Resource):
    def __init__(self):
        # The __init__ method is used to initialize the UserResource class. It is used to create an instance of the reqparse.RequestParser class and add the required arguments to the parser.
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')
  

    @marshal_with(user_fields)
    def get(self, id):
        # The get method is used to get a user by id. It is used to query the user with the given id from the database. It is used to return the user object and the status code 200.
        user = User.query.filter_by(id=id).first()
        if not user:
            # If the user with the given id does not exist, abort with the status code 404 and the error message.
            abort(404, message=f'User with id {id} not found.')
        return user, 200
        
      
    @marshal_with(user_fields)
    def put(self, id):
        # The put method is used to update a user by id. It is used to parse the request data using the reqparse module. It is used to query the user with the given id from the database. It is used to update the user object with the new data. It is used to commit the changes to the database. It is used to return the updated user object and the status code 200.
        from tracker import db
        # The args variable is used to parse the request data using the reqparse module.
        args = self.parser.parse_args()
        # Get the user with the given id from the database
        user = User.query.filter_by(id=id).first()
        if not user:
            # If the user with the given id does not exist, abort with the status code 404 and the error message.
            abort(404, message=f'User with id {id} not found.')
        user.email = args['email']
        user.password_hash = args['password']
        db.session.commit()
        return user, 200
      
    def delete(self, id):
        # The delete method is used to delete a user by id. It is used to query the user with the given id from the database. It is used to delete the user object from the database. It is used to commit the changes to the database. It is used to return the status code 204.
        from tracker import db
        user = User.query.filter_by(id=id).first()
        if not user:
            # Abort if the user with the given id does not exist
            abort(404, message=f'User with id {id} not found.')
        db.session.delete(user)
        db.session.commit()
        return '', 204

# Create the DataResource class
class DataResource(Resource):
    def __init__(self):
        # The __init__ method is used to initialize the DataResource class. It is used to create an instance of the reqparse.RequestParser class and add the required arguments to the parser.
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('systolic', type=int, required=True, help='Systolic is required')
        self.parser.add_argument('diastolic', type=int, required=True, help='Diastolic is required')
        self.parser.add_argument('pulse', type=int, required=True, help='Pulse is required')
        self.parser.add_argument('user_id', type=int, required=True, help='User id is required')


    @marshal_with(data_fields)
    def post(self):
        # The post method is used to create a new data entry. It is used to parse the request data using the reqparse module. It is used to create a new data object and add it to the database. It is used to commit the changes to the database. It is used to return the new data object and the status code 201.
        from tracker import db
        # The args variable is used to parse the request data using the reqparse module.
        args = self.parser.parse_args()
        # Create a new data object
        data = Data(systolic=args['systolic'], diastolic=args['diastolic'], pulse=args['pulse'], user_id=args['user_id'])
        db.session.add(data)
        db.session.commit()
        return data, 201
      
    @marshal_with(data_fields)
    def get(self):
        # The get method is used to get all the data entries. It is used to query all the data entries from the database. It is used to return the list of data entries and the status code 200.
        data = Data.query.all()
        return data, 200
    