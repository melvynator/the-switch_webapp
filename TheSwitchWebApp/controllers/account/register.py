from flask import Blueprint, request, render_template, redirect, url_for
from TheSwitchWebApp.forms.account.account import LoginForm, SignupForm, InitializeAccountForm, RegisterAccountForm
from TheSwitchWebApp.sercives.verify_email_account import verify_email_account
from TheSwitchWebApp.lib.SecureMessage import SecureMessage

import json
import requests
import config

register_endpoint = Blueprint('register', __name__, url_prefix='/register_account')


@register_endpoint.route('/', methods=['GET'])
def display_signup_form():
    error = None
    form = InitializeAccountForm(request.form)
    return render_template("auth/register.html", form=form, error=error)


@register_endpoint.route('/', methods=['POST'])
def process_signup_form():
    form = InitializeAccountForm(request.form)
    # Verify the sign in forms
    if form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        # TODO add exception if the email doesn't land
        response = verify_email_account(first_name, last_name, email)
        return render_template("auth/register.html", form=form)
    else:
        return render_template("auth/register.html", form=form)


@register_endpoint.route('/<string:token>/verify', methods=['GET'])
def display_register_form(token):
    error = None
    # TODO add exception if the token is not decrypt
    decrypted_token = SecureMessage().decrypt(token)
    user_data = json.loads(decrypted_token)
    user_data["token"] = token
    form = RegisterAccountForm()
    return render_template("auth/account_validation.html", form=form, error=error, user_data=user_data)


@register_endpoint.route('/<string:token>/verify', methods=['POST'])
def register_account(token):
    form = RegisterAccountForm(request.form)
    if form.validate_on_submit():
        password = form.password.data
        password_verification = form.password_verification.data
        if password != password_verification:
            return redirect(url_for('register.display_register_form', token=token))
        else:
            decrypted_token = SecureMessage().decrypt(token)
            # TODO exception if decrypt doesn't work
            user_data = json.loads(decrypted_token)
            user_data["password"] = password
            print(user_data)
            response = requests.post(config.API_URL + "/api/v1/accounts", json=user_data)
            if response.status_code == 200:
                return redirect(url_for('account.signin'))
            else:
                return redirect(url_for('register.process_signup_form'))
    else:
        return redirect(url_for('general.home'))
