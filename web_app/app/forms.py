from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf import Form
from wtforms.fields.html5 import DateField
from wtforms.fields import SelectField
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


class SynastryForm(FlaskForm):
    signs = [
        ('', ''),
        ('Aries', 'Aries'), ('Taurus', 'Taurus'),
        ('Cancer', 'Cancer'), ('Gemini', 'Gemini'),
        ('Leo', 'Leo'), ('Virgo', 'Virgo'),
        ('Libra', 'Libra'), ('Scorpio', 'Scorpio'),
        ('Sagittarius', 'Sagittarius'), ('Capricorn', 'Capricorn'),
        ('Aquarius', 'Aquarius'), ('Pisces', 'Pisces'),
    ]
    sun1 = SelectField("Sun", choices=signs, coerce=str)
    sun2 = SelectField("Sun", choices=signs, coerce=str)
    moon1 = SelectField("Moon", choices=signs, coerce=str)
    moon2 = SelectField("Moon", choices=signs, coerce=str)
    rising1 = SelectField("Rising", choices=signs, coerce=str)
    rising2 = SelectField("Rising", choices=signs, coerce=str)
    mercury1 = SelectField("Mercury", choices=signs, coerce=str)
    mercury2 = SelectField("Mercury", choices=signs, coerce=str)
    venus1 = SelectField("Venus", choices=signs, coerce=str)
    venus2 = SelectField("Venus", choices=signs, coerce=str)
    mars1 = SelectField("Mars", choices=signs, coerce=str)
    mars2 = SelectField("Mars", choices=signs, coerce=str)
    jupiter1 = SelectField("Jupiter", choices=signs, coerce=str)
    jupiter2 = SelectField("Jupiter", choices=signs, coerce=str)
    saturn1 = SelectField("Saturn", choices=signs, coerce=str)
    saturn2 = SelectField("Saturn", choices=signs, coerce=str)
    node1 = SelectField("North Node", choices=signs, coerce=str)
    node2 = SelectField("North Node", choices=signs, coerce=str)
    submit = SubmitField("Match!")



##
