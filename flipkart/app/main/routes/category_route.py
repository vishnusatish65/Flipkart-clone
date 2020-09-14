from flask import Blueprint
from flask import request
import json
import jwt
import time
from ..services.category_services import addcategory

category = Blueprint('category',__name__)

@category.route('/')
#api to get list of products category
def home():
    return 'flipkart category home'


@category.route('/add', methods=['POST'])
#api to add a category
def add_category():
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data["expire"] > time.time():
        result = addcategory(data["user_id"])
        if result:
            return {"message":"category added"}
        else:
            return{"message":"error"}
    else:
        return{"message":"timeout"}
