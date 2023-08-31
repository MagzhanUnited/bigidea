from app import app, jwt
from flask import request
from db import UserDB, User
from client import get_access_token
from flask import jsonify
import json
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user
from flask_jwt_extended import create_access_token, create_refresh_token
import bcrypt
# from flask_jwt_extended import set_access_cookies, set_refresh_cookies


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()

@app.route('/login', methods=['POST'])
def login():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    try:
        access_token = get_access_token(email=data['email'], password=data['password'])
    except:
        return "ERROR WHILE GETTING ACCESS TOKEN", 500
    if access_token is None:
        return 'wrong credentials', 401
    user = UserDB(email=data['email'], password=data['password'], access_token=access_token).make_connection().save_user()
    # jwt_token = create_access_token(identity=user)
    access_token = create_access_token(identity=user)
    # refresh_token = create_refresh_token(identity=user)
    # return jsonify({"jwt_token":jwt_token}), 200
    response = jsonify({"jwt_token":access_token})
    # set_refresh_cookies(response, refresh_token)
    # set_access_cookies(response, access_token)
    return response


@app.route("/who_am_i", methods=["GET"])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    return jsonify(
        id=current_user.id,
        access_token=current_user.access_token,
        email=current_user.email
    )
