from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

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
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user", usr=user))
    else:
        return render_template('login.html')

@app.route('/<user>')
def user():
    return f'<h1></h1>'

if __name__ == "__main__":
    app.run(debug=True)