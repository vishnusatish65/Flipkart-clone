from app.main.models.categorymodel import Category
from app.main.models.productmodel import Products, ProductsMeta, db
from flask import request
import json
import jwt
import time

def add_product(user_id):
    #adding a product
    try:
        product_name= request.json["product_name"]
        user_id= user_id
        category_id= request.json["category_id"]
        product = Products(product_name=product_name, user_id=user_id, category_id=category_id)
        db.session.add(product)
        db.session.commit()

        price = request.json["price"]
        description = request.json["description"]
        product_id = product.product_id
        image = request.json["image"]
        product_meta = ProductsMeta(price=price, description=description, product_id=product_id,image = image)
        db.session.add(product_meta)
        db.session.commit()

        return True
    except:
        return False

def delete_product(product_id):
    #deleting a product
    try:
        db.engine.execute("DELETE from product_meta WHERE product_id = '%s'"%(product_id))
        db.engine.execute("DELETE FROM products WHERE product_id = '%s'"%(product_id))
        return True
    except:
        return False
    
def edit_product(product_id):
    #editing product details
    try:
        price = request.json["price"]
        description = request.json["description"] 
        image = request.json["image"]
        db.engine.execute("UPDATE product_meta SET price = '%s', description = '%s', image = '%s'WHERE product_id = '%s'"%(price,description,image,product_id))

        return True
    except:
        return False

def product_owner(product_id):
    #to get product owner details
    try:
        product_owner = db.engine.execute("SELECT user_id FROM products WHERE product_id = '%s'"%(product_id)).first()
        return product_owner.user_id
    except:
        return False

def get_product():
    product_list =[]
    for u in db.session.query(Products).all():
        # getting metadata
        x = db.session.query(ProductsMeta).filter(ProductsMeta.product_id==u.product_id).first()
        metadata = {}
        metadata["price"] = x.price
        metadata["description"] = x.description
        metadata["image"]= x.image
        dict1={}
        dict1["product_id"] = u.product_id
        dict1['product_name'] = u.product_name
        category_object = db.engine.execute("SELECT c.* FROM category c JOIN treepath t on (c.category_id = t.ancestor) WHERE t.decendent='%s'"%(u.category_id))
        listing = []
        for z in category_object:
            listing.append(z.category)
        dict1['category_id'] = listing
        dict1["metadata"] = metadata
        product_list.append(dict1)

    return product_list

def search_product_name(product_name):
    product_list =[]
    for u in db.session.query(Products).filter(Products.product_name==product_name).all():
        # getting metadata
        x = db.session.query(ProductsMeta).filter(ProductsMeta.product_id==u.product_id).first()
        metadata = {}
        metadata["price"] = x.price
        metadata["description"] = x.description
        metadata["image"]= x.image
        dict1={}
        dict1["product_id"] = u.product_id
        dict1['product_name'] = u.product_name
        category_object = db.engine.execute("SELECT c.* FROM category c JOIN treepath t on (c.category_id = t.ancestor) WHERE t.decendent='%s'"%(u.category_id))
        listing = []
        for z in category_object:
            listing.append(z.category)
        dict1['category_id'] = listing
        dict1["metadata"] = metadata
        product_list.append(dict1)

    return product_list

def search_product_category(category):
    #searching for a product with category
    product_list = get_product()
    final_list = []
    for i in product_list:
        if category in  i["category_id"]:
            final_list.append(i)
    
    return final_list