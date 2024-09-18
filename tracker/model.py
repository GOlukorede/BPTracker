# Description: This file contains the model classes for the database tables. The User class is used to store user information and the Data class is used to store the blood pressure data. The User class has a one-to-many relationship with the Data class. The User class also has a password_hash property that is used to store the hashed password in the database. The password_hash property uses the bcrypt library to hash the password. The check_password method is used to check if the plain password matches the hashed password in the database.

from tracker import db, login_manager
from tracker import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    # The load_user function is used to load the user from the database using the user_id. It is used to return the user object with the specified user_id.
    return User.query.get(int(user_id))

# Create the User class
class User(db.Model, UserMixin):
    # The User class is used to create the user table in the database. It is used to define the columns of the user table. It is used to define the one-to-many relationship between the User and Data tables. It is used to define the password_hash property to store the hashed password in the database. It is used to define the check_password method to check if the plain password matches the hashed password in the database.
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    data = db.relationship('Data', backref='user', lazy=True)
    
    @property
    def password_hash(self):
        # The password_hash property is used to store the hashed password in the database. It is used to return the hashed password.
        return self.password
      
    @password_hash.setter
    def password_hash(self, password):
        # The password_hash setter is used to hash the password using the bcrypt library. It is used to set the hashed password in the database.
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_password(self, plain_password):
        # The check_password method is used to check if the plain password matches the hashed password in the database. It is used to return True if the plain password matches the hashed password, otherwise it returns False.
        return bcrypt.check_password_hash(self.password, plain_password)
    
# Create the Data class
class Data(db.Model):
    # The Data class is used to create the data table in the database. It is used to define the columns of the data table. It is used to define the foreign key relationship between the Data and User tables.
    id = db.Column(db.Integer, primary_key=True)
    systolic = db.Column(db.Integer, nullable=False)
    diastolic = db.Column(db.Integer, nullable=False)
    pulse = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)