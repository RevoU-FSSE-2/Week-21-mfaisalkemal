from flask import Blueprint, request
import jwt, os
from user.models import User

user_blp = Blueprint("user", __name__)

@user_blp.route('/', methods=['GET'])
def get_user_profile():
    token = request.headers.get('Authorization')
    payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms='HS256')

    user_id = payload['user_id']
    user = User.query.get(user_id)

    if not user:
        return {"error", "Username not found!"}, 404
    
    return{
        'id': user.id
    }