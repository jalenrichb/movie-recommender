from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'littlebites'
app.permanent_session_lifetime = timedelta(days=1)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommendations')
def recommendations():
    return render_template("recommendations.html")

@app.route('/list')
def list():
    return render_template("list.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login succesful")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in! ")
            return redirect(url_for("user"))
        return render_template('login.html')

@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        
        return render_template('user.html')
    else:
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    flash("Logged out successfully!", "info")
    session.pop("user", None)
    
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)