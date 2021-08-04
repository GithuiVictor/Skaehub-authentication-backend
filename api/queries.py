from flask import jsonify
from .models import User
import jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def resolve_user_authentication(obj, info, email, password):
    try:
        user = User.query.get(email)
        if email != user.email or password != user.password:
            payload = {
                "success": False,
                "errors": ["Bad username or password"]
            }
        else:
            access_token = create_access_token(identity=email)
            payload = {
                "success": True,
                "token": jsonify(access_token=access_token),
                "user": user.to_dict()
            }

    except:  # error 401 wrong credentials
        payload = {
            "success": False,
            "errors": ["Unauthorized user"]
        }

    return payload

@convert_kwargs_to_snake_case
@jwt_required()
def resolve_user_profile(obj, info, user_id):
    try:
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        status = jsonify(logged_in_as=current_user), 200
        user = User.query.get(user_id)
        payload = {
            "success": True,
            "status": status,
            "user": user.to_dict()
        }

    except:  # error 401 wrong credentials
        payload = {
            "success": False,
            "errors": ["Unauthorized user"]
        }

    return payload