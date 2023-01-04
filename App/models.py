import sqlalchemy
from App import app, bcrypt, login_manager, db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    # password = db.Column(db.String(length=10), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    points = db.Column(db.Integer(), default=0)
    # matches = db.relationship('Matches', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'User {self.username}: {self.email}'

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class Matches(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    team1 = db.Column(db.String(length=16), nullable=False)
    team1_score = db.Column(db.Integer())
    team2 = db.Column(db.String(length=16), nullable=False)
    team2_score = db.Column(db.Integer())
    group = db.Column(db.String(length=4), nullable=False)
    # owner 

    # def __init__(self, team1, team2, group):
    #     self.team1 = team1
    #     self.team2 = team2
    #     self.group = group

    def __repr__(self):
        return f'Match nr {self.id}: {self.team1} vs {self.team2}'

