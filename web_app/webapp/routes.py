from flask import render_template, url_for, flash, redirect, request
from webapp import app, db, bcrypt
from webapp.forms import MatchForm, ChartForm, SynastryForm
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


@app.route("/synastry", methods=["POST","GET"])
def synastry():
    form = SynastryForm()
    if form.validate_on_submit():
        chart1 = [
            form.sun1.data, form.moon1.data, form.rising1.data,
            form.mercury1.data, form.venus1.data, form.mars1.data,
            form.jupiter1.data, form.saturn1.data, form.node1.data,
        ]
        chart2 = [
            form.sun2.data, form.moon2.data, form.rising2.data,
            form.mercury2.data, form.venus2.data, form.mars2.data,
            form.jupiter2.data, form.saturn2.data, form.node2.data,
        ]
        data = full_chart(chart1, chart2)
        return render_template("matched.html", data=data, form=form)
    return render_template("synastry.html", form=form)



##
