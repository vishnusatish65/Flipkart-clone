from app.main import db

class Comment(db.Model):
    #creating comment table database
    __tablename__= "comment"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment = db.Column(db.Text)
    product_id = db.Column(db.Integer,db.ForeignKey('products.product_id'))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)