from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf import Form
from wtforms.fields.html5 import DateField
from wtforms.fields import SelectField
import datetime as dt


def default_date():
    return dt.datetime.strptime("1990-01-01", "%Y-%m-%d")


def hours():
    return [
        (0, '12:00am'), (1, '1:00am'), (2, '2:00am'), (3, '3:00am'),
        (4, '4:00am'), (5, '5:00am'), (6, '6:00am'), (7, '7:00am'),
        (8, '8:00am'), (9, '9:00am'), (10, '10:00am'), (11, '11:00am'),
        (12, '12:00pm'), (13, '1:00pm'), (14, '2:00pm'), (15, '3:00pm'),
        (16, '4:00pm'), (17, '5:00pm'), (18, '6:00pm'), (19, '7:00pm'),
        (20, '8:00pm'), (21, '9:00pm'), (22, '10:00pm'), (23, '11:00pm')
    ]


def timezones():
    return [
        (-11, 'UTC−11:00 American Samoa'), (-10, 'UTC−10:00 Hawaii'), (-9, 'UTC−09:00 Alaska'),
        (-8, 'UTC−08:00 Seattle'), (-7, 'UTC−07:00 Denver'), (-6, 'UTC−06:00 Mexico City'),
        (-5, 'UTC−05:00 New York'), (-4, 'UTC−04:00 Nova Scotia'), (-3, 'UTC−03:00 Buenos Aires'),
        (-2, 'UTC−02:00 Atlantic'), (-1, 'UTC−01:00 Azores'), (0, 'UTC±00:00 London'),
        (1, 'UTC+01:00 Paris'), (2, 'UTC+02:00 Athens'), (3, 'UTC+03:00 Moscow'),
        (4, 'UTC+04:00 Dubai'), (5, 'UTC+05:00 Yekaterinburg'), (6, 'UTC+06:00 Almaty'),
        (7, 'UTC+07:00 Krasnoyarsk'), (8, 'UTC+08:00 Irkutsk'), (9, 'UTC+09:00 Tokyo'),
        (10, 'UTC+10:00 Sydney'), (11, 'UTC+11:00 Vanuatu'), (12, 'UTC+12:00 Auckland'),
        (13, 'UTC+13:00 Samoa'), (14, 'UTC+14:00 Kiribati')
    ]


def signs():
    return [
        ('', ''),
        ('Aries', 'Aries'), ('Taurus', 'Taurus'),
        ('Cancer', 'Cancer'), ('Gemini', 'Gemini'),
        ('Leo', 'Leo'), ('Virgo', 'Virgo'),
        ('Libra', 'Libra'), ('Scorpio', 'Scorpio'),
        ('Sagittarius', 'Sagittarius'), ('Capricorn', 'Capricorn'),
        ('Aquarius', 'Aquarius'), ('Pisces', 'Pisces'),
    ]


class MatchForm(FlaskForm):
    hrs = hours()
    tzones = timezones()
    bday1 = DateField("Birth Date", format="%Y-%m-%d", default=default_date())
    bday1_hr = SelectField("Birth Hour", choices=hrs, default=hrs[12][0], coerce=int)
    bday1_tz = SelectField("Timezone", choices=tzones, default=tzones[11][0], coerce=int)
    bday2 = DateField("Birth Date", format="%Y-%m-%d", default=default_date())
    bday2_hr = SelectField("Birth Hour", choices=hrs, default=hrs[12][0], coerce=int)
    bday2_tz = SelectField("Timezone", choices=tzones, default=tzones[11][0], coerce=int)
    submit = SubmitField("Match!")


class ChartForm(FlaskForm):
    hrs = hours()
    tzones = timezones()
    bday = DateField("Birth Date", format="%Y-%m-%d", default=default_date())
    hr = SelectField("Birth Hour", choices=hrs, default=hrs[12][0], coerce=int)
    tz = SelectField("Timezone", choices=tzones, default=tzones[11][0], coerce=int)
    submit = SubmitField("Calculate!")


class SynastryForm(FlaskForm):
    signs = signs()
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
