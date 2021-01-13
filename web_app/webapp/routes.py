from flask import render_template, url_for, flash, redirect, request
from webapp import app, db, bcrypt
from webapp.forms import RegistrationForm, SigninForm, QuestionForm, MatchForm, ChartForm
from webapp.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from .syn_calc import *


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Log In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")


@app.route("/questions", methods=["GET", "POST"])
def questions():
    form = QuestionForm()
    if form.validate_on_submit():
        flash(f"{form.name.data} sent", "success")
        return redirect(url_for("home"))
    return render_template("questions.html", title="Question", form=form)


@app.route("/html")
def blog():
    return render_template("html.html", title="Blog")


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
