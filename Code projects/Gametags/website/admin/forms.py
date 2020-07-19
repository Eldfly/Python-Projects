from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed


class CreateGameForm(FlaskForm):

    game = StringField('Name', validators=[DataRequired()])
    code = StringField('Code', validators=[DataRequired()])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg','png', 'jepg'])])
    create_game = SubmitField('Create game')
