from wtforms import StringField, SubmitField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from website.models import Games

def game_query():
    return Games.query.order_by(Games.game.asc())

class CreateTagForm(FlaskForm):

    tag = StringField('Tag*', validators=[DataRequired()])

    game = QuerySelectField(query_factory=game_query, get_label="game")
    server = StringField('Server*', validators=[DataRequired()])
    create_tag = SubmitField('Create Tag')
