from website import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    profile_image = db.Column(db.String(64),nullable=False, default='default_profile.png')
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    tag = db.relationship('Tags',backref='user', lazy=True)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, email, username, password, is_admin=False):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.is_admin = is_admin

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'{self.username}'

class Tags(db.Model):

    __tablename__ = 'tags'

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    tag = db.Column(db.String(140), nullable=False)
    game = db.Column(db.String(140), nullable=False)
    server = db.Column(db.String(140), nullable=False)


    def __init__(self,tag,game,server,user_id):
        self.tag = tag
        self.game = game
        self.server = server
        self.user_id = user_id

    def __repr__(self):
        return f'{self.game}'

class Games(db.Model):

    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(64),nullable=False, default='gaming1.jpg')
    game = db.Column(db.String(140), nullable=False, unique=True)
    code = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self,game, code, image):
        self.game = game
        self.code = code
        self.image = image

    def __repr__(self):
        return '{}'.format(self.code)

    def __str__(self):
        return '{}'.format(self.code)
