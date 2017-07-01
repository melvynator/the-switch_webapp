# Import Security messaging
from TheSwitchWebApp.lib.SecureMessage import SecureMessage
import config
import os, base64

# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import a module / component using its blueprint handler variable (mod_auth)
from TheSwitchWebApp.controllers.account.account import account_endpoint as account
from TheSwitchWebApp.controllers.account.register import register_endpoint as register
from TheSwitchWebApp.module_general.controllers import module_general as general_module
from TheSwitchWebApp.module_user_management.controllers import module_user_management as user_module


# Sample HTTP error handling
@app.errorhandler(404)
def not_found():
    return render_template('404.html'), 404

# Register blueprint(s)
app.register_blueprint(account)
app.register_blueprint(general_module)
app.register_blueprint(user_module)
app.register_blueprint(register)


# Generate the key
#os.environ["SECRET_KEY"] = str(SecureMessage().generate_key(), 'iso-8859-1')
#print(config.SECRET_KEY)

# Build the database:
# This will create the database file using SQLAlchemy
db.drop_all()
db.create_all()
