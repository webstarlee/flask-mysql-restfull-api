from flask import Flask, jsonify, render_template
import os
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS, cross_origin
from models import User
from datetime import timedelta
import resources
from config import sql_config

app = Flask(__name__)

app = Flask(__name__,
            static_folder = "./template/assets",
            template_folder = "./template")

CORS(app, resources={r"/api/*": {"origins": "*"}}, CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SQLALCHEMY_DATABASE_URI'] = sql_config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "SH13.20230616.Lee.Schedule"  # Change this!
jwt = JWTManager(app)
api = Api(app)

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()

with app.app_context():
    from db import db
    db.init_app(app)
    db.create_all()

api.add_resource(resources.SignIn, '/api/signin')
api.add_resource(resources.Info, '/api/info')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
