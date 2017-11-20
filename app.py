#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from flask import Flask,render_template,make_response,redirect,jsonify,request,url_for,send_from_directory
from werkzeug import secure_filename
from flask.ext.login import current_user,login_required,login_user,logout_user,confirm_login,fresh_login_required
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
import hashlib
import time
import config.app_config as app_config
import psutil
from flask_sqlalchemy import SQLAlchemy
import os
import pymongo
import sys
import random
import json
app_config.load_config()


app = Flask(__name__)
app.config['SECRET_KEY'] = app_config.CACHE['secret_key']
app.config['MONGODB_SETTINGS'] = {'HOST':app_config.CACHE['db_address']+':'+app_config.CACHE['db_port'],'DB':app_config.CACHE['mongodb_name']}
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:uplooking@localhost/mysqlHs'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = MongoEngine(app)
mysqldb = SQLAlchemy(app)

flask_bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)

from application.auth.auth import auth_flask_login
from application.monitor.monitor import monitor
from application.photos.photos import photos
from application.game.game import game
app.register_blueprint(auth_flask_login)
app.register_blueprint(monitor)
app.register_blueprint(photos)
app.register_blueprint(game)


@app.route('/')
def index():
    if current_user.is_authenticated():
        resp = make_response(render_template('index.html'))
    else:
        resp = make_response(render_template('login.html'))
    return resp

@app.route('/scmap')
def scmap():
    resp = make_response(render_template('scmap.html'))
    return resp

@app.route('/scmap_highchart')
def scmap_highchart():
    resp = make_response(render_template('scmap_highchart.html'))
    return resp

@app.route('/city_level_1')
def city_level_1():
    conn = pymongo.Connection(host='127.0.0.1',port=27017)
    db = conn.txdata
    enName = request.args.get('name').encode('raw_unicode_escape')
    condition = {"enName":enName}
    print(condition)
    res = db.city_level_1.find_one(condition,{'_id':0,'delaycount':1,'totcount':1,'name':1})
    print(jsonify(res))
    return jsonify(res)

@app.route('/osstat')
def osstat():
    #cpu = str(psutil.virtual_memory().percent)
    dict = {}
    mem_tot =  float(psutil.virtual_memory().total)
    mem_free = float(psutil.virtual_memory().free)
    percent = mem_free/mem_tot * 100
    percent_cpu = str(percent + random.uniform(0,1))
    percent = str(percent + random.uniform(0,1))
    dict['cpu'] = percent_cpu
    dict['mem'] = percent
    return jsonify(dict)
