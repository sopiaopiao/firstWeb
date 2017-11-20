#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import current_app,Blueprint,jsonify,render_template,abort,request,flash,redirect,url_for,make_response,Flask,url_for,send_from_directory
from werkzeug import secure_filename
import config.app_config as app_config
import os
app_config.load_config()
import sys

game = Blueprint('game',__name__,template_folder='templates')
@game.route('/gameinfo',methods=['GET','POST'])
def gameinfo():
    resp = make_response(render_template('gameweb.html'))
    return resp

@game.route('/record',methods=['GET','POST'])
def record():
    print request.form
    resp = make_response(render_template('gameweb.html'))
    return resp
