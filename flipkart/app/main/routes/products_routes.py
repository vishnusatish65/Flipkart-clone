from flask import Blueprint
from flask import request
import json
import jwt
import time
from ..services.product_services import add_product, delete_product, edit_product, product_owner, get_product, search_product_name, search_product_category

product = Blueprint('product',__name__)

@product.route('/')
#api to get list of all products
def all_products():
    x = get_product()
    return json.dumps(x)

@product.route('/add', methods=['POST'])
#api to add a product
def add_products():
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token,key)
    if data['type']== "Owner":
        if data["expire"] > time.time():
            #add_product module from product_services in services folder
            result = add_product(data["user_id"])
            if result:
                return {"message":"product added"}
            else:
                return {"message":"logic error"}
        else:
            return{"mesage":"timed out"}
    else:
        return{"message":"not registered as owner"}

@product.route('/delete/<product_id>', methods=['DELETE'])
#api to delete a product
def delete_products(product_id):
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token,key)
    if data['user_id']==  product_owner(product_id):
        if data["expire"] > time.time():
            if delete_product(product_id):
                return {"message":"product deleted"}
            else:
                return {"message":"logic error"}
        else:
            return{"mesage":"timed out"}
    else:
        return{"message":"not registered as owner"}

@product.route('/edit/<product_id>', methods=['PATCH'])
#api to edit 
def edit_products(product_id):
    auth_token = request.headers["auth_token"]
    key = 'secret'
    data = jwt.decode(auth_token,key)
    if data['user_id']== product_owner(product_id):
        if data["expire"] > time.time():
            if edit_product(product_id):
                return {"message":"product edited"}
            else:
                return {"message":"logic error"}
        else:
            return{"mesage":"timed out"}
    else:
        return{"message":"not registered as owner"}

@product.route('/<var>')
#api to search for a product
def search_products(var):
    if var == "search":
        product_name = request.args.get('product',default="", type= str)
        list_of_products = search_product_name(product_name)
        return json.dumps(list_of_products)
    elif var =="filter":
        category_name = request.args.get('category',default="",type=str)
        list_of_products = search_product_category(category_name)
        return json.dumps(list_of_products)
