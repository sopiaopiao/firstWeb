#!/user/bin/python
# -*- coding: utf-8 -*-

import os
import json

VOYAGER_HOME=os.getenv('VOYAGER_HOME','/opt/voyager')
CONFIG_NAME="myweb.json"
CACHE={}


def load_config():
    global CACHE,rootPrefix,mongodb_name,token,MONGODB_CONFIG
    if len(CACHE) == 0:
        f = file(VOYAGER_HOME+"/conf/"+CONFIG_NAME)
        CACHE = json.load(f)
      
        if CACHE['mongodb_name']:
            mongodb_name = CACHE['mongodb_name']
        if CACHE['db_address']:
            db_address = CACHE['db_address']
        if CACHE['db_port']:
            db_port = CACHE['db_port']
        if CACHE['secret_key']:
            secret_key = CACHE['secret_key']
    else:
        print 'config already load'

load_config()
   
        
