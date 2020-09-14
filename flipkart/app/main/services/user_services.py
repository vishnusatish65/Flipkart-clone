from app.main.models.usermodel import User, db
from flask import request
import json
import jwt
import time

def add_user():
    #registering a new user
    try:
        username = request.json["username"]
        fullname = request.json["fullname"]
        password = request.json["password"]
        Type = request.json["type"]
        contact = request.json["contact"]
        user = User(username=username, fullname=fullname,Password=password, Type =Type ,Contact=contact)
        db.session.add(user)
        db.session.commit()
        return True
    except:
        return False

def login():
    #login a user
    username = request.json["username"]
    password = request.json["password"]

    user = db.engine.execute("SELECT id, username, password, Type FROM users WHERE username = '%s'"%(username)).first()
    if user:
        if user.password == password:
            payload = {"user_id":user.id, "message":"correct password", 'expire':time.time()+3600, "type":user.Type }
            key = 'secret'
            encode_jwt = jwt.encode(payload,key)
            
            return {'auth_token':encode_jwt.decode(),"message":"logged_in", 'user_id':user.Type}
        else:
            return {"message":"login failed"}
    else:
        return {"message":"login failed, Incorrect username"}


