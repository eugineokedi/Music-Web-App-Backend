from flask import Flask
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from flask import request, session,make_response
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)
api = Api(app)
CORS = CORS(app)