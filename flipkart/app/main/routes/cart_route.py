from flask import Blueprint
from flask import request
import json
import jwt
import time
from ..services.cart_service import add_cart, get_cart, buy_cart

cart = Blueprint('cart', __name__)


@cart.route('/add/<product_id>', methods=['POST'])
#api to add products to user cart
def add_user_cart(product_id):
    #user verification
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data["expire"] > time.time():
        x = add_cart(data['user_id'], product_id)
        if x:
            return {"status": True, "message": "product added to cart"}
        else:
            return {"status": False, "message": "server error"}
    else:
        {"status": True, "message": "timed out"}


@cart.route('/')
#api to get all items in user cart
def user_cart():
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data["expire"] > time.time():
        x = get_cart(data["user_id"])
        if x:
            return{"status": True, "products": x}
        elif len(x) == 0:
            return {"status": True, "message": "No items in cart"}
        else:
            return{"status": False, "message": "server error"}
    else:
        {"status": True, "message": "timed out"}


@cart.route("/buy", methods=['POST'])
#api to order items in the cart
def buy_carts():
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data["expire"] > time.time():
        x = buy_cart(data["user_id"])
        if x:
            return {"status": True, "message": "order received"}
        else:
            return{"status": False, "message": "server error"}
    else:
        {"status": True, "message": "timed out"}
