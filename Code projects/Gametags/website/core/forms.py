from wtforms import StringField,SubmitField
from flask_wtf import FlaskForm


class SearchUserForm(FlaskForm):

    username = StringField('Username')
    search = SubmitField('Search')
