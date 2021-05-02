from flask import render_template, url_for, flash, redirect, request
from webapp import app, db, bcrypt
from webapp.forms import MatchForm, ChartForm
from .syn_calc import *


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/match", methods=["POST","GET"])
def match():
    form = MatchForm()
    if form.validate_on_submit():
        b1 = form.bday1.data.strftime("%Y-%m-%d")
        b2 = form.bday2.data.strftime("%Y-%m-%d")
        data = display_synastry_cleaner_code(b1, b2)
        return render_template("matched.html", data=data, form=form)
    return render_template("match.html", form=form)


@app.route("/chart", methods=["POST","GET"])
def chart():
    form = ChartForm()
    if form.validate_on_submit():
        bday = form.bday.data.strftime("%Y-%m-%d")
        data = display_single_chart(bday)
        return render_template("chart_calc.html", data=data, form=form)
    return render_template("chart.html", form=form)



##
