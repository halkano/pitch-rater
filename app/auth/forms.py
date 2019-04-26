from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, BooleanField, SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError



class LoginForm(FlaskForm):
    email = StringField('Enter your email', validators=[Required(), Email()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
