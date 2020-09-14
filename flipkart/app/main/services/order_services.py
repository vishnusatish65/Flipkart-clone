from app.main.models.ordermodel import Order, OrderProduct, db
from app.main.models.productmodel import Products, ProductsMeta
from flask import request
import json
import jwt
import time


def get_order(user_id):
    #get user order details
    x = db.engine.execute("SELECT * FROM orders WHERE user_id = '%s'"%(user_id))
    order_list = []
    for row in x:
        dict1 = {}
        dict1["order_id"] = row.id
        dict1["Amount"] = row.amount
        dict1["payment_status"] = row.payment_status
        dict1["status"] = row.status
        product_details = []
        y = db.engine.execute("SELECT * FROM order_product WHERE order_id='%s'"%(row.id))
        for row in y:
            x =  db.session.query(ProductsMeta).filter(ProductsMeta.product_id==row.product_id).first()
            metadata = {}
            metadata["product_id"] = row.product_id
            metadata["price"] = x.price
            metadata["description"] = x.description
            metadata["image"]= x.image
            product_details.append(metadata)
        dict1["procut_detail"] = product_details
        order_list.append(dict1)

    return order_list
