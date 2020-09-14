from flask import Blueprint
from flask import request
import json
import jwt
import time
from ..services.comment_services import add_comment, add_votes, down_votes, get_comments

comment = Blueprint('comment',__name__)

@comment.route("/add",methods=["POST"])
#api to add a comment to a product
def add_comments():
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token,key)
    if data["expire"] > time.time():
        add_comment(data["user_id"])
        return{"message":"comment added"}
    else:
        return{"status": True, "message": "timed out"}


@comment.route("/<comment_id>", methods=['POST'])
#api to upvote or downvote a comment
def add_vote(comment_id):
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token,key)
    vote = request.args.get('vote', default="upvote", type=str)
    if vote == 'upvote':
        x = add_votes(comment_id)
        return {"status": True,"message": "comment liked"}
    else:
        x = down_votes(comment_id)
        return {"status": True, "message": "comment dislike"}
        return 

@comment.route("/search/<product_id>", methods=['POST'])
#api to get comments for the products
def get_comment(product_id):
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token,key)
    if data["expire"]> time.time():
        x = get_comments(product_id)
        if x :
            return {"status": True, "Product_id": product_id, "comments": x}
        elif len(x) == 0:
            return{"status":True, "message":"No comments"}
        else:
            return{"status": False,"message": "server error" }
    else:
        return {"status": True, "Message":"Connection timed_out"}
