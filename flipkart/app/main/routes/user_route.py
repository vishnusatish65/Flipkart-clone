from flask import Blueprint
from ..services.user_services import add_user, login

user = Blueprint('user',__name__)

@user.route('/')
def home():
    return 'flipkart home'

@user.route('/register',methods=['POST'])
#api to add a new user
def new_user():
    result = add_user()
    if result:
        return {"message":"user added"}
    else:
        return {"message":"error"}

@user.route('/login',methods=['POST'])
#api to login user
def login_user():
    data = login()
    if data["message"] == "logged_in":
        return {"message":"login success", "auth_token":data['auth_token']}
    else:
        return {"message":"login failed"}