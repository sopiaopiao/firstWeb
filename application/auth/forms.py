# -*- coding: utf-8 -*-

import models
from flask.ext.mongoengine.wtf import model_form
from wtforms.fields import *
from flask.ext.mongoengine.wtf.orm import validators

user_form = model_form(models.User,exclude=['password'])

class SignupForm(user_form):
    password = PasswordField('Password',validators=[validators.Required(),validators.EqualTo('confirm',message='密码不匹配')])
    confirm = PasswordField('confirm')
 

class LoginForm(user_form):
    password = PasswordField('Password',validators=[validators.Required()])
