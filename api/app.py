from flask import Flask, render_template
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
from database import Create_and_set_database

app = Flask(__name__)

db = Create_and_set_database()


def make_list(data):
    list_links = [data[i]["link"].split("=")[1] for i in range(len(data))]
    return list_links


@app.route('/')
def index():
    data_azure = db.select("AZURE")
    data_sre = db.select("SRE")
    data_python = db.select("PYTHON")
    #link_youtube = data_azure[0]["link"]
    azure_videos = make_list(data_azure) + \
        make_list(data_sre) + make_list(data_python)
    # Script qui recupere cours
    # return json.dumps(liste_links)
    return render_template("main.html", all_videos=azure_videos)


@app.route('/cours/<name>')
# This will  serve and fetch all cours in /cours/python  /azure /sre / etc..
def view_individual_cours(name):
    data_cours = db.select(name.upper())
    video_links = make_list(data_cours)
    print(video_links)
    # Script qui recupere cours
    return render_template("cours.html", data=video_links)

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


@app.errorhandler(Exception)
def server_error(err):
    return render_template('notfound.html'), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
