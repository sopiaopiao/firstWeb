# -*- coding: utf-8 -*-

import models
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self,username=None,password=None,active=True,id=None,key=None):
        self.username = username
        self.password = password
        self.active = active
        self.key = key
        self.isAdmin = False
        self.id = None
     
    def save(self):
        newUser = models.User(username=self.username,password=self.password,active=self.active,key=self.key) 
        newUser.save()
        print "new user id = %s"  % newUser.id
        self.id = newUser.id
        return self.id 

    def get_by_username_w_password(self,username):
        print(username)
        try:
            dbUser = models.User.objects.get(username=username)
            print(dbUser.username+'get ok')
            if dbUser:
                self.username = dbUser.username
                self.active = dbUser.active
                self.id = dbUser.key
                self.password = dbUser.password
                self.key = dbUser.key
                print(self.username,self.active,self.id)
                print(self)
                return self
            else:
                return None
                print('info is none')
        except:
            print "there was an error"
            return None
  
    def get_by_id(self,id):
        dbUser = models.User.objects.with_id(id)
        if dbUser:
            self.username = dbUser.username
            self.active = dbUser.active
            self.id = dbUser.id
            self.key = dbUser.key
            return self
        else:
            return None
        
