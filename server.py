import datetime
import uuid

from flask import Flask, render_template, session, request, url_for, redirect
#from werkzeug.security import check_password_hash, generate_password_hash

from user import user

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'


@app.route('/')
def home():
    return render_template('home.html', page_title='gusty.bike')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":
        if not request.form["email"] or not request.form["username"] or not request.form["password"]:
            return '0'

        email = request.form["email"]
        username = request.form["username"]
        pw = request.form["password"]

        if user.create(email, pw, username, "gusty_bike"):
            return '1'
        else:
            return '0'

    return render_template('register.html', page_title='gusty.bike')


@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.html', page_title='gusty.bike')


@app.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
    if request.method == "POST":
        if not request.form["username"] or not request.form["password"]:
            return '0'  # response 0 = fail

        name = request.form["username"]
        pw = request.form["password"]

        if user.check_password(name, pw):
            #authenticate
            return '1' # response 1 = success
        else:
            return '0' # reponse 0 = fail
    else:
        return None # return nothing because the request isnt valid


@app.route('/post')
def post():
    return 'hello'


# start the server
if __name__ == '__main__':
    app.run()