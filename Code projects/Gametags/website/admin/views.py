from flask import render_template, url_for, flash, redirect, request, Blueprint
from website.admin.forms import CreateGameForm
from website import db
from website.models import Games
from website.admin.picture_handler import add_game_pic

admin = Blueprint('admin', __name__)


@admin.route('/admin_home')
def admin_home():
    registered_games = Games.query.all()
    return render_template('admin_home.html', registered_games=registered_games)


#function create game on admin page
@admin.route('/create_game', methods=['GET', 'POST'])
def create_game():

    form = CreateGameForm()
    registered_games = Games.query.all()

    if form.validate_on_submit():

        if form.picture.data:
            game_code = form.code.data
            pic = add_game_pic(form.picture.data,game_code)


        game = Games(game=form.game.data, code=form.code.data, image=pic)

        db.session.add(game)
        db.session.commit()

        return redirect(url_for('admin.admin_home'))

    return render_template('admin_createGame.html', form=form, registered_games=registered_games)

#delete game
@admin.route('/<int:game_id>/delete_game', methods=['GET', 'POST'])
def delete_game(game_id):
    game = Games.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    flash('Game deleted')
    return redirect(url_for('admin.admin_home'))
