from app.main.models.categorymodel import Category,db
from flask import request
import json
import jwt
import time

def addcategory(user_id):
    #adding a new category to database
    try:
        user_id = user_id
        category = request.json["category"]
        parent_id = request.json["parent_id"]
        category = Category(user_id=user_id,category=category, parent_id =parent_id)
        db.session.add(category)
        db.session.commit()
        x = category.category_id
        db.engine.execute("INSERT INTO Treepath(ancestor,decendent) SELECT ancestor, '%s' FROM Treepath WHERE decendent='%s' UNION ALL SELECT '%s','%s'"%(x,parent_id,x,x))
            
        return True
    except:
        return False
