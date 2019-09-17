from flask import session as login_session
from flask import Flask, Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
import json
import jwt
from datetime import datetime, timedelta
from models.users import UsersModel
from app import app

login_routes = Blueprint('login_routes', __name__)

@login_routes.route("/login", methods=["POST"])
def login():
    
    data = request.get_json(silent=True)
    email = data["email"]
    password = data["password"]
    
    user = UsersModel().authenticate(
        email=email,
        password=password
    )
    if not user:
        return jsonify({'message': 'Invalid Credentials', 'authenticated': False})

    # set the session of the user
    login_session["user_id"] = str(user["_id"])
    print(f"user id: {login_session}")
    response = jsonify(
        {
        "token": jwt.encode(
            {
                'sub': user['email'],
                'iat':datetime.utcnow(),
                'exp': datetime.utcnow() + timedelta(minutes=30)
            },
            app.config['SECRET_KEY']
        ).decode('UTF-8'),
        "user": {
            "id": str(user['_id']),
            "username": user['username'],
            "email": user['email']
        },
        'authenticated': 'true'
        }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@login_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)
    username = data["username"]
    print(f"inside reg function")
    email = data["email"]
    password = data["password"]
    password_confirmation = data["password_confirmation"]

    # Check that user doesn't exist already
    if not UsersModel.check_user(email):
        print(f"This email is used")
        return jsonify({'message': 'A user with that email already exists', 'authenticated': False})
    print(f"The email is ok")

    # Check password confirmation
    if password!=password_confirmation:
        return jsonify({'message': 'Password not equal to password confirmation', 'authenticated': False})

    user, user_id = UsersModel.register(
        username=username,
        email=email,
        password=password
    )

    # login user after registration
    response = jsonify(
        {
        "token": jwt.encode(
            {
                'sub': user['email'],
                'iat':datetime.utcnow(),
                'exp': datetime.utcnow() + timedelta(minutes=30)
            },
            app.config['SECRET_KEY']
        ).decode('UTF-8'),
        "user": {
            "id": str(user_id),
            "username": user['username'],
            "email": user['email']
        },
        'authenticated': 'true'
        }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

    
