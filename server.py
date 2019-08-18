#!/usr/bin/env python3.7
from flask import Flask, request
from flask_cors import CORS, cross_origin
from app import app
import json
import settings 


#route imports
from routes.api import api_routes
from routes.login import login_routes

app.register_blueprint(api_routes)
app.register_blueprint(login_routes)
cors = CORS(app)

if __name__ == "__main__":
    app.run(
        host = '0.0.0.0', 
        port = 3001,
        debug=True
    )
    