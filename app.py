#!/usr/bin/env python3.7
from flask import Flask

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['ENV'] = 'development'
app.config['SECRET_KEY'] = 'cheese'

