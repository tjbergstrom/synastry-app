from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webapp.models import User
from flask_wtf import Form
from wtforms.fields.html5 import DateField


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Please choose a new one")

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("That email is already registered. Please enter a different one")


class SigninForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign in")


class QuestionForm(FlaskForm):
    name = StringField("Subject", validators=[DataRequired()])
    description = TextAreaField("Ask me anything", validators=[DataRequired()])
    to = StringField("To", validators=[DataRequired()])
    submit = SubmitField("Send", validators=[DataRequired()])


class MatchForm(FlaskForm):
    bday1 = DateField("", format="%Y-%m-%d")
    bday2 = DateField("", format="%Y-%m-%d")
    submit = SubmitField("Match!")


##
