from flask import request, jsonify
import flask_restful
from functools import wraps
import jwt
import os
from src.model.db import User
from flask_cors import cross_origin


def authenticate(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return func(current_user, *args, **kwargs)

    return decorator


class Resource(flask_restful.Resource):
    method_decorators = [authenticate, cross_origin]
