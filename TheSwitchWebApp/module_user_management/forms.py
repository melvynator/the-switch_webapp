from flask_wtf import FlaskForm as Form

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField, TextAreaField, FileField # BooleanField

# Import Form validators
from wtforms.validators import InputRequired, Email, EqualTo


class ChangeEmailForm(Form):
    old_email = StringField('Old email Address', [Email(), InputRequired(message='New E-mail adress is mandatory')])
    new_email = StringField('New email Address', [Email(), InputRequired(message='Old E-mail adress is mandatory')])
    password = PasswordField('Password', [InputRequired(message='Enter a password')])


class ChangePasswordForm(Form):
    old_password = PasswordField('Password', [InputRequired(message='Enter an old password')])
    new_password = PasswordField('Password', [InputRequired(message='Enter a new password')])
    password_verification = PasswordField('Password', [EqualTo('new_password', message='Passwords should be the same'),
                                                       InputRequired(message='Enter a verification password')])


class RecipientForm(Form):
    recipient_name = StringField('Recipient name', [InputRequired(message='First name is mandatory')])
    recipient_email = StringField('Email Address', [Email(), InputRequired(message='E-mail adress is mandatory')])


class DocumentForm(Form):
    document_name = StringField('Document name', [InputRequired(message='First name is mandatory')])
    document_details = TextAreaField("Document details", [InputRequired(message='Detail are needed')])
    file = FileField("File")
