from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from webapp import login
from webapp import db


class User(UserMixin, db.Document):
    username = db.StringField(max_length=64)
    email = db.StringField(max_length=120)
    password_hash = db.StringField(max_length=128)


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()
