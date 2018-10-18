import datetime
import uuid

from flask import Flask, render_template, session, request, url_for, redirect
# from werkzeug.security import check_password_hash, generate_password_hash

from database import database
from user import user

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

db = database()


@app.route('/')
def home():
    db.connect()

    if session.get('authenticated'):
        client = user(session['user_id'], db)
        render_template('home.html', page_title='gusty.bike', client=client)

    return render_template('home.html', page_title='gusty.bike')


@app.route('/login')
def login():

    if session.get('authenticated'):
        return redirect(url_for('home'))

    return render_template('login.html', page_title='gusty.bike')


@app.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
    if request.method == "POST":

        db.connect()

        request_type = request.form["type"]

        if request_type == "l":
            if not request.form["username"] or not request.form["password"]:
                return '2'  # response 2 = field blank

            username = request.form["username"]
            password = request.form["password"]

            uid = user.login(username, password, db)

            if uid == 0:
                return '0' # response 0 = fail
            else:
                session['user_id'] = uid
                session['authenticated'] = True

                return '1'  # response 1 = SUCCESS!

        if request_type == "r":
            if not request.form["username"] or not request.form["email"] or \
                    not request.form["password"] or not request.form["password2"]:
                return '2'  # response 2 = field blank

            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            password2 = request.form["password2"]

            if '@' not in email or '.' not in email:
                return '3'  # response 3 = email not formatted correctly

            if password != password2:
                return '4'  # response 4 = passwords do not match

            if not len(password) >= 6:
                return '5'  # response 5 = password not long enough

            if not username.isalnum() or len(username) >= 30:
                return '6'  # response 6 = username does not fit criteria

            if user.exists(username, db):
                return '0'  # response 7 user already exists

            session['user_id'] = user.create(email, password, username, db)
            session['authenticated'] = True

            return '1'  # response 1 = SUCCESS!
    else:
        return None  # return nothing because the request isnt valid


@app.route('/post')
def post():
    return 'hello'


@app.route('/admin')
def admin():

    if not session.get('authenticated'):
        return redirect(url_for('home'))

    db.connect()

    client = user(session['user_id'], db)

    if not client.rank >= 3:
        return redirect(url_for('home'))

    return render_template('admin.html', page_title='gusty.bike', client=client)


@app.route('/admin/sliders/new')
def new_slider():
    if not session.get('authenticated'):
        return redirect(url_for('home'))

    db.connect()

    client = user(session['user_id'], db)

    if not client.rank >= 3:
        return redirect(url_for('home'))

    return render_template('admin_sliders_new.html', page_title='gusty.bike')


# start the server
if __name__ == '__main__':
    app.run()