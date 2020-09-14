from flask import Blueprint
from flask import request
import json
import jwt
import time
from ..services.wishlist_services import add_wishlist, get_wishlist

wishlist = Blueprint('wishlist', __name__)


@wishlist.route('/add/<product_id>', methods=['POST'])
#api to add product to user wishlist
def add_user_wishlist(product_id):
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data["expire"] > time.time():
        x = add_wishlist(data['user_id'], product_id)
        if x:
            return {"status": True, "message": "product added to wishlist"}
        else:
            return {"status": False, "message": "server error"}
    else:
        return{"status": True, "message": "timed out"}


@wishlist.route('/')
#api to get all products in user wishlist
def user_wishlist():
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data["expire"] > time.time():
        x = get_wishlist(data["user_id"])
        if x:
            return{"status": True, "products": x}
        elif len(x) == 0:
            return {"status": True, "message": "No items in wish list"}
        else:
            return{"status": False, "message": "server error"}
    else:
        return{"status": True, "message": "Timed Out"}
