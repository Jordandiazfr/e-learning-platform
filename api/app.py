from flask import Flask, render_template
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
from database import Create_and_set_database

app = Flask(__name__)

db = Create_and_set_database()


@app.route('/')
def index():
    # Script qui recupere cours
    return render_template("main.html")


@app.route('/cours/<name>')
# This will  serve and fetch all cours in /cours/python  /azure /sre / etc..
def data(name):
    my_data = db.fetchDATAfile(name)
    # Script qui recupere cours
    return json.dumps(my_data)

# Retourne un formulaire


@app.route('/insert-playlist', methods=['GET'])
def playlist_panel():
    return render_template("insert-cours.html")

# Recupere l'infor des form et les print, lorsque ils sont gardes dans les variables x, y et apres il redirige
# ver l'index


@app.route('/insert-playlist', methods=['POST'])
def insert_playlist():
    x = request.form['c_name']
    y = request.form['c_code']
    print(x)
    print(y)
    return index()


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
