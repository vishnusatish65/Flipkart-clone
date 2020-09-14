from app.main.routes.products_routes import product
from app.main import db


class Order(db.Model):
    # creating order table in the database
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    payment_status = db.Column(db.String(50))
    status = db.Column(db.String(50))
    amount = db.Column(db.Integer)


class OrderProduct(db.Model):
    #creating relationship table with order table and product table
    __tablename__ = "order_product"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
