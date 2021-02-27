# Interact with the operating system
import os
import json
import requests

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
# Creates temporary files and directories
from tempfile import mkdtemp
# HTTP Exceptions
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required

# This current file represents a flask application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Hey you have to provide a username :(", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Hey you have to provide a password :(", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/")
@login_required
def index():
    return render_template("index.html")


# FOR REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Check if method is POST
    if request.method == "POST":
        # User does not enter a username
        if not request.form.get("username"):
            return apology("Hey provide a username :)", 403)
        # User does not enter a password
        elif not request.form.get("password"):
            return apology("Hey provide a password :)", 403)
        # If the password the user entered does not match the confirmation password
        elif request.form.get("password") != request.form.get("confirmation password"):
            return apology("ERROR: confirmation password and the password you entered are not the same", 403)

        username = db.execute("SELECT username FROM users WHERE username = ?", request.form.get("username"))

        # check if the username is already taken
        if len(username) > 0:
            return apology("Sorry! Username Taken", 403)

        db.execute("INSERT INTO users (username, hash) VALUES (:username, :password)", username=request.form.get("username"), password=generate_password_hash(request.form.get("password")))

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/services", methods=["GET", "POST"])
def services():
    return render_template("services.html")


