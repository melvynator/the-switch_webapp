# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import json

# Import module forms
from TheSwitchWebApp.module_user_management.forms import RecipientForm

import requests

module_user_management = Blueprint('user_management', __name__, url_prefix='/account')


@module_user_management.route('/recipients/', methods=['GET', 'POST'])
def recipients():
    error = None
    form = RecipientForm(request.form)
    if form.validate_on_submit():
        name = form.recipient_name.data
        email = form.recipient_email.data
        print("Here call the API to add the recipients")
        # API call
    print("Here call the API to get the saved recipients of the user")
    return render_template("management/recipients.html", form=form, error=error)


@module_user_management.route('/documents/', methods=['GET', 'POST'])
def documents():
    error = None
    form = RecipientForm(request.form)
    if form.validate_on_submit():
        name = form.recipient_name.data
        email = form.recipient_email.data
        print("Here call the API to add the recipients")
        # API call
    print("Here call the API to get the saved recipients of the user")
    return render_template("management/documents.html", form=form, error=error)


@module_user_management.route('/settings/', methods=['GET', 'POST'])
def settings():
    error = None
    form = RecipientForm(request.form)
    if form.validate_on_submit():
        name = form.recipient_name.data
        email = form.recipient_email.data
        print("Here call the API to add the recipients")
        # API call
    print("Here call the API to get the saved recipients of the user")
    return render_template("management/settings.html", form=form, error=error)
