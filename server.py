import datetime
import uuid

from flask import Flask, render_template, session, request, url_for, redirect
#from werkzeug import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'


@app.route('/')
def home():
    return render_template('home.html', page_title='gusty.bike')


@app.route('/post')
def post():
    return 'hello'


# start the server
if __name__ == '__main__':
    app.run()