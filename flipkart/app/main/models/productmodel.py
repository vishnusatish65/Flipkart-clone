from app.main.routes.category_route import category
from app.main import db

class Products(db.Model):
    #creating product table in database
    __tablename__ = "products"
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.category_id"))

class ProductsMeta(db.Model):
    # create product meta details table with one to one relationship with products table
    __tablename__ = "product_meta"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    description =db.Column(db.Text())
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
    image = db.Column(db.Text())