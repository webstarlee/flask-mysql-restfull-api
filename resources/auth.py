import json
from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required, current_user
from models import User, Profile
from util.encoder import AlchemyEncoder
from util.logz import create_logger

class Info(Resource):
    def __init__(self):
        self.logger = create_logger()

    @jwt_required()  # Requires dat token
    def get(self):
        # We can now access our sqlalchemy User object via `current_user`.
        return jsonify(
            no=current_user.no,
            fullname=current_user.fullname,
            username=current_user.username,
            user_id=current_user.user_id,
        )

class SignIn(Resource):
    def __init__(self):
        self.logger = create_logger()

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

    def post(self):
        data = SignIn.parser.parse_args()
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).one_or_none()
        if not user or not user.check_password(password):
            return {'message': 'Invalid Credentials.'}, 401
        
        access_token = create_access_token(identity=user)
        return_user = {
            "fullname": user.fullname,
            "username": user.username,
            "user_id": user.user_id,
            "token": access_token
        }
        return jsonify(return_user)