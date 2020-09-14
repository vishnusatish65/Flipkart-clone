from app.main import db

class Category(db.Model):
    #creating category table in database
    __tablename__= "category"
    category_id =db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    parent_id = db.Column(db.Integer) 

class TreePath(db.Model):
    #creating relationship table for many to many relationship
    __tablename__="treepath"
    ancestor = db.Column(db.Integer, db.ForeignKey('category.category_id'),primary_key=True)
    decendent = db.Column(db.Integer, db.ForeignKey('category.category_id'),primary_key=True)
    company = db.relationship("Category", foreign_keys=[ancestor])
    stakeholder = db.relationship("Category", foreign_keys=[decendent])

