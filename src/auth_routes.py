from flask import Blueprint, request, make_response, jsonify
from werkzeug.security import check_password_hash
from src.model.db import User
import jwt
import datetime
import os


auth_routes = Blueprint("auth_routes", __name__)


def jwt_payload(user):
    result = {'public_id': user.public_id}
    if os.getenv("TOKEN_EXPIRATION_TIME_MINUTES") != '0':
        result["exp"] = datetime.datetime.utcnow() + datetime.timedelta(
            minutes=int(os.getenv("TOKEN_EXPIRATION_TIME_MINUTES")))
    return result


@auth_routes.route('/get_token', methods=['POST'])
def get_token():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'Authentication': 'login required"'})

    user = User.query.filter_by(name=auth.username).first()
    if check_password_hash(user.password, auth.password):
        token = jwt.encode(jwt_payload(user), os.getenv("SECRET_KEY"), "HS256")
        return jsonify({'token': token})

    return make_response('could not verify', 401, {'Authentication': '"login required"'})
