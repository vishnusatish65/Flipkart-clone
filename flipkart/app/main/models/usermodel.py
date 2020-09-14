from app.main import db

class User(db.Model):
    #creating user table in database
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    fullname = db.Column(db.String(50))
    Password = db.Column(db.String(50))
    Type = db.Column(db.String(50))
    Contact = db.Column(db.Integer)

