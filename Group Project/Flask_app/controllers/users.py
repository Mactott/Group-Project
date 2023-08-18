from flask import render_template,redirect,request,session, flash, url_for
from Flask_app import app
from Flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/loggin", methods=["post"])
def loggin():
    email = request.form["email"]
    password_raw = request.form["password"]
    user = User.loggin(email)
    session["email"] = email
    if user:
        if bcrypt.check_password_hash(user.password, password_raw):
            print(user)
            return redirect("/my_team")
        else:
            flash("Incorrect Password","invalidpw")
            return redirect("/")
    else:
        flash("Invalid Email","invalidpw")
        return redirect("/")