from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf import Form
from wtforms.fields.html5 import DateField
import datetime as dt


def default_date():
    return dt.datetime.strptime("1990-01-01", "%Y-%m-%d")


class MatchForm(FlaskForm):
    bday1 = DateField("", format="%Y-%m-%d", default=default_date())
    bday2 = DateField("", format="%Y-%m-%d", default=default_date())
    submit = SubmitField("Match!")


class ChartForm(FlaskForm):
    bday = DateField("", format="%Y-%m-%d", default=default_date())
    submit = SubmitField("Calculate!")



##
