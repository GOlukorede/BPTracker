# Description: This file contains the form classes for the registration, login, and data submission forms.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length as length, ValidationError
from tracker.model import User


# Create the RegisterForm class
class RegisterForm(FlaskForm):
    # The RegisterForm class is used to create the registration form. It is used to define the form fields and the form validators. It is used to validate the email field to check if the email already exists in the database. It is used to display the error message if the email already exists. It is used to define the form submit button.
    def validate_email(self, email):
        # The validate_email method is used to validate the email field. It is used to check if the email already exists in the database. It is used to raise a validation error if the email already exists.
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists. Please use a different email.')
    
    firstname = StringField('First Name: ', validators=[length(min=2, max=20), DataRequired()])
    lastname = StringField('Last Name: ', validators=[length(min=2, max=20), DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password: ', validators=[DataRequired(), length(min=6)])
    password2 = PasswordField('Confirm Password: ', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Register')
    

# Create the LoginForm class
class LoginForm(FlaskForm):
    # The LoginForm class is used to create the login form. It is used to define the form fields and the form validators. It is used to define the form submit button.
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')


# Create the DataForm class
class DataForm(FlaskForm):
    # The DataForm class is used to create the data submission form. It is used to define the form fields and the form validators. It is used to define the form submit button.
    systolic = IntegerField('Systolic Pressure: ', validators=[DataRequired()])
    diastolic = IntegerField('Diastolic Pressure: ', validators=[DataRequired()])
    pulse = IntegerField('Pulse: ', validators=[DataRequired()])
    submit = SubmitField('Submit Data')