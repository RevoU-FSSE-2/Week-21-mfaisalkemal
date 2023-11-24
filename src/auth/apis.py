from flask import Blueprint, request
from common.bcrypt import bcrypt
from user.models import User
from db import db

auth_blp = Blueprint("auth", __name__)

@auth_blp.route("/registration", methods=["POST"])
def register():
    data = request.get_json()

    username = data["username"]
    password = data["password"]
    bio = data["bio"]

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password, bio=bio)
    db.session.add(new_user)
    db.session.commit()

    return{
        'id': new_user.id,
        'username': new_user.username,
        'bio': new_user.bio
    }