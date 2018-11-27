from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_mongoengine import MongoEngine


app = Flask(__name__, static_folder="public")
app.config.from_object(Config)
db = MongoEngine(app)
login = LoginManager(app)
login.login_view = 'login'


from webapp import routes, models
