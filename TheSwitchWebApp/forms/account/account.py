# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm as Form

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import InputRequired, Email, EqualTo


# Define the login forms (WTForms)

class LoginForm(Form):
    email = StringField('Email Address', [Email(), InputRequired(message='Forgot your email address?')])
    password = PasswordField('Password', [InputRequired(message='Enter a password')])


class SignupForm(Form):
    first_name = StringField('First name', [InputRequired(message='First name is mandatory')])
    last_name = StringField('Last name', [InputRequired(message='Last name is mandatory')])
    email = StringField('Email Address', [Email(), InputRequired(message='E-mail adress is mandatory')])
    password = PasswordField('Password', [InputRequired(message='Enter a password')])
    password_verification = PasswordField('Password', [EqualTo('password', message='Passwords should be the same'),
                                                       InputRequired(message='Enter a verification password')])


class InitializeAccountForm(Form):
    first_name = StringField('First name', [InputRequired(message='First name is mandatory')])
    last_name = StringField('Last name', [InputRequired(message='Last name is mandatory')])
    email = StringField('Email Address', [Email(), InputRequired(message='Forgot your email address?')])


class RegisterAccountForm(Form):
    password = PasswordField('Password', [InputRequired(message='Enter a password')])
    password_verification = PasswordField('Password', [EqualTo('password', message='Passwords should be the same'),
                                                       InputRequired(message='Enter a verification password')])
