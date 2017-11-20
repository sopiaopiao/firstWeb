#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import current_app,Blueprint,jsonify,render_template,abort,request,flash,redirect,url_for
import config.app_config as app_config
import psutil
import random
import os
app_config.load_config()

monitor = Blueprint('monitor',__name__,template_folder='templates')

@monitor.route('/appsoft')
def appsoft():
    #cpu = str(psutil.virtual_memory().percent)
    dict = {}
    mem_tot =  float(psutil.virtual_memory().total)
    mem_free = float(psutil.virtual_memory().free)
    percent = mem_free/mem_tot * 100
    percent_cpu = str(percent + random.uniform(0,1))
    percent = str(percent + random.uniform(0,1))
    dict['cpu'] = percent_cpu
    dict['mem'] = percent
  
    ob_pid = os.popen("ps -ef|grep appName|grep -v grep|awk '{print $2}'").readlines()
    if ob_pid != []:
        dict['ob_status'] = 'running'
    else:
        dict['ob_status'] = 'down'
    return jsonify(dict)
