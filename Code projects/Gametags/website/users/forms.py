from flask import url_for, flash, render_template,request,redirect
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf import FlaskForm


class SignupForm(FlaskForm):


    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_pass', message='Password must match')])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired()])
    admin = BooleanField('Admin')


    def check_email(self,field):
        if User.query.filter_by(email=form.field.data).first():
            raise ValidationError('This email is already registered')


    def check_username(self, field):
        if User.query.filter_by(username=form.field.data).first():
            raise  ValidationError('This username already exists in our system')

    signup = SubmitField('Sign up')


class SigninForm(FlaskForm):


    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    signin = SubmitField('Sign in')
