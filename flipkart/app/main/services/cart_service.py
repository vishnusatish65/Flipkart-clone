from app.main.models.ordermodel import Order, OrderProduct
from app.main.models.cartmodels import Cart, db
from app.main.models.productmodel import Products, ProductsMeta
from flask import request
import json
import jwt
import time


def add_cart(user_id, product_id):
    #adding product to user cart
    try:
        user_id = user_id
        product_id = product_id
        cart = Cart(user_id=user_id, product_id=product_id)
        db.session.add(cart)
        db.session.commit()
        return True
    except:
        return False


def get_cart(user_id):
    #get all product in user cart
    final_list = []
    user_products = db.engine.execute(" SELECT cart.user_id, cart.product_id, products.product_name, products.category_id FROM cart JOIN products ON products.product_id=cart.product_id where cart.user_id = '%s'"%(user_id))
    for product in user_products:
        dict1 = {}
        dict1["product_id"] = product.product_id
        dict1["product_name"] = product.product_name
        x = db.session.query(ProductsMeta).filter(ProductsMeta.product_id==product.product_id).first()
        metadata = {}
        metadata["price"] = x.price
        metadata["description"] = x.description
        metadata["image"]= x.image
        dict1["metadata"] = metadata
        category_object = db.engine.execute("SELECT c.* FROM category c JOIN treepath t on (c.category_id = t.ancestor) WHERE t.decendent='%s'"%(product.category_id))
        listing = []
        for z in category_object:
            listing.append(z.category)
        dict1['category_id'] = listing
        final_list.append(dict1)

    return final_list


def buy_cart(user_id):
    #to order all products in the cart
    try:
        products_in_cart = []
        amount = 0
        x = db.engine.execute("SELECT cart.product_id, product_meta.price FROM cart JOIN product_meta ON cart.product_id=product_meta.product_id WHERE cart.user_id='%s'"%(user_id))
        for row in x:
            dict1 = {}
            dict1["product_id"] = row.product_id
            dict1["price"] = row.price
            amount += row.price
            products_in_cart.append(dict1)

        payment_status = request.json["payment_status"]
        status = request.json["status"]
        amount = amount
        order = Order(user_id=user_id, payment_status=payment_status, status=status, amount=amount)
        db.session.add(order)
        db.session.commit()
        order_id = order.id
        for row in products_in_cart:
            order_product = OrderProduct(order_id=order_id, product_id=row["product_id"])
            db.session.add(order_product)
            db.session.commit()

        db.engine.execute("DELETE FROM cart WHERE user_id='%s'"%(user_id))
        return True
    except:
        return False
