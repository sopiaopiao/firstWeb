#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import current_app,Blueprint,jsonify,render_template,abort,request,flash,redirect,url_for
from user import User
from app import flask_bcrypt,login_manager
from flask.ext.login import (current_user,login_required,login_user,logout_user,confirm_login,fresh_login_required)
import forms
import config.app_config as app_config
app_config.load_config()
 
auth_flask_login = Blueprint('auth_flask_login',__name__,template_folder='templates')

@auth_flask_login.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST" and "username" in request.form:
        username = request.form["username"]
        userObj = User()
        user = userObj.get_by_username_w_password(username)
        if user and flask_bcrypt.check_password_hash(user.password,request.form["password"]) and user.is_active:
            print(user.is_active)
            remember = request.form.get("remember","no") == "yes" 
            
            if login_user(user,remember=remember):
                flash("Logged in!")
                return render_template("logined.html")
            else:
                flash("unable to log you in")
    return render_template("login.html")

@auth_flask_login.route("/register",methods=["GET","POST"])
def register():
    registerForm = forms.SignupForm(request.form)
#    current_app.logger.info(request.form)
    if request.method == 'POST' and registerForm.validate() == False:
        current_app.logger.info(registerForm.errors)
        return "uhoh registration error"

    elif request.method == 'POST' and registerForm.validate():
        username = request.form['username']
        password_hash = flask_bcrypt.generate_password_hash(request.form['password'])
        user = User(username,password_hash,key='')
        
        try:
            user.save()
            if login_user(user,remember="no"):
                flash("Logged in !") 
                return render_template("logined.html")
            else:
                flash("unable to log you in")  
        except Exception as e:
            print(e.message)
            flash("unable to register with that username address") 
    templateData = {'form':registerForm}
    return render_template('/register.html',**templateData)

@auth_flask_login.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out")
    return render_template('/login.html')

@login_manager.unauthorized_handler
def unauthorized_callback():
    return render_template('/login.html')

@login_manager.user_loader
def load_user(id):
    if id is None:
        return render_templates("/login.html")
        user = User()
        user.get_by_id(id)
        if user.is_active():
            return user
        else:
            return None















