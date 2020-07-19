from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from website.tags.forms import CreateTagForm
from website import db
from website.models import Tags, Games

gametags = Blueprint('gametags', __name__)


#create tag login required
@gametags.route('/createtag', methods=['GET', 'POST'])
@login_required
def create_tag():

    form = CreateTagForm()

    if form.validate_on_submit():

        game = str(form.game.data)

        tag = Tags(tag=form.tag.data, game=game, server=form.server.data, user_id=current_user.id)
        db.session.add(tag)
        db.session.commit()
        return redirect(url_for('users.home'))

    return render_template('create_tag.html', form=form)

#delete
@gametags.route('/delete/<int:tag_id>', methods=['GET', 'POST'])
@login_required
def delete_tag(tag_id):

        tag = Tags.query.get_or_404(tag_id)

        if tag.user_id != current_user.id:
            abort(403)

        db.session.delete(tag)
        db.session.commit()
        flash('tag deleted')
        return redirect(url_for('users.home'))
