#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import current_app,Blueprint,jsonify,render_template,abort,request,flash,redirect,url_for,make_response,Flask,url_for,send_from_directory
from werkzeug import secure_filename
import config.app_config as app_config
import os
app_config.load_config()
import sys

photos = Blueprint('photos',__name__,template_folder='templates')


@photos.route('/travel',methods=['GET','POST'])
def travel():
    whichAlbum = request.form.get('showpic')
    imgList = []
    if whichAlbum is None:
        whichAlbum = 'HeartStone'
    path1 = '/opt/voyager/apps/myweb/static/uploadIMG/' + whichAlbum
    path2 = '../static/uploadIMG/' + whichAlbum
    for (dirpath, dirnames, filenames) in os.walk(path1):
        for filename in filenames:
            abspath = path2
            imgList.append(os.path.join(abspath,filename))
    resp = make_response(render_template('photos.html',imgList=imgList))
    return resp

#####upload start


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = '/opt/voyager/apps/myweb/static/uploadIMG'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@photos.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER,
                               filename)


@photos.route('/uploadpic', methods=['GET', 'POST'])
def upload_file():
#    print(request.method)
#    print request.form.get('album')
    album = request.form.get('blankRadio')
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            UPLOAD_FOLDER_2 = UPLOAD_FOLDER + '/' + album
            try:
                file.save(os.path.join(UPLOAD_FOLDER_2, filename))
            except:
                os.mkdir(UPLOAD_FOLDER_2)
                file.save(os.path.join(UPLOAD_FOLDER_2, filename))

          #  file_url = url_for('uploaded_file', filename=filename)
            return make_response(render_template('photos.html'))
    return make_response(render_template('photos.html'))
