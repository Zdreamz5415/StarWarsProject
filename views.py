from flask import Blueprint, app, render_template, redirect, url_for


views = Blueprint(__name__, "views")


@views.route("/")
def homepage():
    return render_template("index.html", name = "stephen")



@views.route("/jedi")
def jedi_page():
    return render_template("jedi.html")

@views.route("/sith")
def sith_page():
    return render_template("sith.html")

@views.route("/lightsabers")
def lightsabers_page():
    return render_template("lightsabers.html")

@views.route("/planets")
def planets_page():
    return render_template("planets.html")

@views.route("/home")

def home_redirect():
    return redirect(url_for("views.homepage"))