from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from website.users.forms import SignupForm, SigninForm
from website import db
from website.models import User, Tags
from sqlalchemy.exc import IntegrityError

users = Blueprint('users', __name__)

#when going to home page of the profile the user will see all their gametags
@users.route('/home')
def home():
    gametags = Tags.query.filter_by(user_id=current_user.id).order_by(Tags.game.asc())
    return render_template('account.html', gametags=gametags)


@users.route('/signup', methods=['GET', 'POST'])
def signup():

    form = SignupForm()

    if form.validate_on_submit():

        user = User(email=form.email.data, username=form.username.data, password=form.password.data, is_admin=form.admin.data)

        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('users.signin'))

        except:
            db.session.rollback()
            return render_template('signup.html', form=form, msg='The data you gave is not unique. Either username or email already exists in the database')

    return render_template('signup.html', form=form)

@users.route('/singin', methods=['GET', 'POST'])
def signin():

    form = SigninForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is None:
            return render_template('signin.html', form=form, msg="Email doesnt exists")
        elif user.check_password(form.password.data) == False:
            return render_template('signin.html', form=form, msg='wrong password')

        elif user.check_password(form.password.data) and user is not None:

            login_user(user)
            print(user.is_admin)

            if user.is_admin:
                return redirect(url_for('admin.admin_home'))
            else:
                next = request.args.get('next')

                if next == None or not next[0]=='/':
                    next = url_for('users.home')

                return redirect(next)

    return render_template('signin.html', form=form)

#logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))
