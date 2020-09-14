from flask import Blueprint
from flask import request
import json
import jwt
import time
from ..services.order_services import get_order

order = Blueprint('order', __name__)


@order.route("/")
#api to get all user's orders
def get_orders():
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data["expire"] > time.time():
        x = get_order(data["user_id"])
        if x:
            return {"status": True, "details": x}
        if len(x) == 0:
            return{"status": True, "message": "not orders to show"}
    else:
        return{"status": True, "message": "timed out"}
