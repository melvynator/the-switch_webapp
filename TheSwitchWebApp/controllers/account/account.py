import json
import requests
import config

from flask import Blueprint, request, render_template, flash, session, redirect, url_for

from TheSwitchWebApp.forms.account.account import LoginForm, SignupForm

account_endpoint = Blueprint('account', __name__, url_prefix='/account')


@account_endpoint.route('/signin/', methods=['GET', 'POST'])
def signin():
    error = None
    form = LoginForm(request.form)
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_info = json.dumps({"password": password, "email": email})
        # API call
        response = requests.post(config.API_URL + "/api/v1/authenticate", json=user_info)
        if response.status_code == 200:
            session["logged_in"] = True
            return redirect(url_for("user_management.recipients"))
        else:
            error = "Login or password incorrect"
    flash("There is a mistake in your id/password")
    return render_template("auth/signin.html", form=form, error=error)


@account_endpoint.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    # Verify the sign in forms
    if form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = form.password.data
        json_user = json.dumps({"first_name": first_name, "last_name": last_name, "email": email, "password": password})
        response = requests.post(config.API_URL + "/api/v1/accounts", json=json_user)
        if response.status_code == 200:
            return redirect(url_for('account.success'))
    return render_template("auth/signup.html", form=form)


@account_endpoint.route('/success/', methods=['GET'])
def success():
    return render_template("auth/signup_successfull.html")
