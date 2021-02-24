from flask import Flask, render_template
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from dbclass import MySqlDb

app = Flask(__name__)

db = MySqlDb("pythonlogin")


@app.route('/')
def index():
    return render_template("main.html")


"""if not session.get('logged_in'):
        return render_template('login.html')
    else: """


""" @app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return index()
 """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
