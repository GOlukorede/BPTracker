# The __init__.py file is used to initialize the Flask application. It is the first file that is executed when the Flask application is run. It is used to create the Flask application instance, the database instance, the bcrypt instance, the login_manager instance, and the API instance. It is also used to register the API resources with the appropriate endpoints. The __init__.py file is also used to import the route module, which contains the route definitions for the Flask application.

# Imports Flask and other necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_restful import Api
import os
from dotenv import load_dotenv
load_dotenv()


# Create an instance of the Flask class and set the configuration options
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_bp.db'
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
api = Api(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
# app.app_context().push()
# Import the model module
from tracker.api_page import UsersResource, UserResource, DataResource

# Register your API resources with the appropriate endpoints
api.add_resource(UsersResource, '/api/users')
api.add_resource(UserResource, '/api/user/<int:id>')
api.add_resource(DataResource, '/api/data')


# Import the route module
from tracker import route
