from flask import render_template, request, Blueprint, redirect, url_for
from website.models import Tags, User
from flask_login import current_user, login_required
from website.core.forms import SearchUserForm


core = Blueprint('core', __name__)


#index page have the searchbox for users
@core.route('/', methods=['GET','POST'])
def index():

    form = SearchUserForm()

    search_string = form.username.data

    if search_string:
        username = User.query.filter_by(username=search_string).first()

        if username is None:
            return render_template('index.html', form=form, username='No user with that username')
        elif username.is_admin == False and username is not None:
            return render_template('index.html', form=form, username=username)
        else:
            return render_template('index.html', form=form, username='No user with that username')

    return render_template('index.html', form=form)


#route when searching for users at index page (/).
@core.route('/<username>')
def search_user(username):

    user = User.query.filter_by(username=username).first_or_404()
    gametags = Tags.query.filter_by(user_id=user.id).order_by(Tags.game.asc())
    return render_template('search_users.html', gametags=gametags, user=user)
