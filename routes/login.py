from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
import json
import jwt
from datetime import datetime, timedelta
from models.users import UsersModel
from app import app

login_routes = Blueprint('login_routes', __name__)

@login_routes.route("/login", methods=["POST"])
@cross_origin(origin='*',headers=['Access-Control-Allow-Origin','*'])
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
    response = {
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
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response