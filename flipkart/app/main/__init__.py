import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#linking the app to database and api's
db = SQLAlchemy()

from app.main.routes.user_route import user as user_blueprints
from app.main.routes.category_route import category as category_blueprints
from app.main.routes.products_routes import product as product_blueprints
from app.main.routes.wishlist_routes import wishlist as wishlist_blueprints
from app.main.routes.cart_route import cart as cart_blueprints
from app.main.routes.order_route import order as order_blueprints
from app.main.routes.comment_routes import comment as comment_blueprints


def create_apps():
    app = Flask(__name__)
    database_password = os.environ.get("DB_PASS")
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:%s@localhost/flipkart"%(database_password)

    db.init_app(app)
    app.register_blueprint(user_blueprints,url_prefix='/user')
    app.register_blueprint(category_blueprints,url_prefix='/category')
    app.register_blueprint(product_blueprints,url_prefix='/product')
    app.register_blueprint(wishlist_blueprints,url_prefix='/wishlist')
    app.register_blueprint(cart_blueprints,url_prefix='/cart')
    app.register_blueprint(order_blueprints,url_prefix='/order')
    app.register_blueprint(comment_blueprints,url_prefix='/comment')

    return app