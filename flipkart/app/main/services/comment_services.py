from app.main.models.productmodel import Products, ProductsMeta, db
from app.main.models.commentmodels import Comment
from flask import request
import json
import jwt
import time


def add_comment(user_id):
    #adding a comment to a product
    product_id = request.json["product_id"]
    comment = request.json["comment"]
    upvotes = 0
    downvotes = 0
    comment = Comment(user_id=user_id, product_id=product_id, comment=comment, upvotes=upvotes, downvotes=downvotes)
    db.session.add(comment)
    db.session.commit()

    return True


def add_votes(data):
    #upvoting a product
    x = db.session.query(Comment).filter(Comment.user_id == data).first()
    x.upvotes += 1
    db.session.commit()
    return x.upvotes


def down_votes(data):
    #downvoting a product
    x = db.session.query(Comment).filter(Comment.id == data).first()
    x.upvotes -= 1
    db.session.commit()
    return x.upvotes


def get_comments(product_id):
    #getting all the comments for a product
    x = db.session.query(Comment).filter(Comment.product_id == product_id).all()
    comment_list = []
    for y in x:
        dict1 = {}
        dict1["user_id"] = y.user_id
        dict1["comment"] = y.comment
        dict1["upvotes"] = y.upvotes
        dict1["downvotes"] = y.downvotes
        comment_list.append(dict1)
    return comment_list
