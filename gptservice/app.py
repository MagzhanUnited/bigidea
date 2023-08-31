from flask import Flask
from flask_cors import CORS
import os
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")  # Change this!
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:magzhan2005@localhost/bigidea'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
# app.config["JWT_COOKIE_SECURE"] = False
CORS(app, origins=['http://127.0.0.1:5173', 'http://localhost:3000', 'http://192.168.1.66:3000' ])

jwt = JWTManager(app)
