from app.main.models.wishlistmodel import Wishlist, db
from app.main.models.productmodel import Products, ProductsMeta
from flask import request
import json
import jwt
import time


def add_wishlist(user_id,product_id):
    #adding product to the wishlist
    try:
        user_id = user_id
        product_id = product_id
        wishlist = Wishlist(user_id=user_id, product_id=product_id)
        db.session.add(wishlist)
        db.session.commit()

        return True
    except:
        return False


def get_wishlist(user_id):
    #get all products in wishlist
    final_list = []
    user_products = db.engine.execute(" SELECT wishlist.user_id, wishlist.product_id, products.product_name, products.category_id FROM wishlist JOIN products ON products.product_id=wishlist.product_id where wishlist.user_id = '%s'" %(user_id))
    for product in user_products:
        dict1 = {}
        dict1["product_id"] = product.product_id
        dict1["product_name"] = product.product_name
        x = db.session.query(ProductsMeta).filter(ProductsMeta.product_id==product.product_id).first()
        metadata = {}
        metadata["price"] = x.price
        metadata["description"] = x.description
        metadata["image"] = x.image
        dict1["metadata"] = metadata
        category_object = db.engine.execute("SELECT c.* FROM category c JOIN treepath t on (c.category_id = t.ancestor) WHERE t.decendent='%s'"%(product.category_id))
        listing = []
        for z in category_object:
            listing.append(z.category)
        dict1['category_id'] = listing
        final_list.append(dict1)

    return final_list
