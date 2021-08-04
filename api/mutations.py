from ariadne import convert_kwargs_to_snake_case
from main import db
from api.models import User

@convert_kwargs_to_snake_case
def resolve_create_user(obj, info, name, email, password):
    try:
        user = User(
            name = name,
            email = email,
            password = password
        )
        db.session.add(user)
        db.session.commit()
        payload = {
            "success": True,
            "user": user.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Something went wrong"]
        }
    return payload