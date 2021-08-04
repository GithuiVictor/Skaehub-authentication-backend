from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

# Create flask app
app = Flask(__name__)

#Configure and add our database
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/user.db"

# This disables tracking modifications of objects and sending signals to the application for every database change. 
# Its a good feature but can cause memory overhead. Its should only be used where necessary.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)

#Set up the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "iuabeui23h087&"
jwt = JWTManager(app)

@app.route('/')
def hello():
    return 'Hello!'