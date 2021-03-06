from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextField, HiddenField 
from wtforms.validators import DataRequired, Length, Email
from flask_login import UserMixin

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', [DataRequired(), Length(min=3, max=25)]) 
    last_name = StringField('Last Name', [DataRequired(), Length(min=3, max=25)])
    username = StringField('Username', [DataRequired(), Length(min=2, max=25)])
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Sign Up')
    
class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Login')