import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345KEY'
#
# ################################
# ###### DATABASE SETUP ##########
# ################################
#
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
db = SQLAlchemy(app)
Migrate(app,db)
#
# ################################
# ###### Login configuration #####
# ################################
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'users.signin'


from website.core.views import core
from website.users.views import users
from website.tags.views import gametags
from website.admin.views import admin
#
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(gametags)
app.register_blueprint(admin)
