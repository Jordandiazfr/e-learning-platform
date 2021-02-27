from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
from database import Create_and_set_database

app = Flask(__name__)

db = Create_and_set_database()


def make_list(data):
    list_links = [data[i]["link"].split("=")[1] for i in range(len(data))]
    return list_links


def make_list_from_link(data):
    list_links = [data[i].split("=")[1] for i in range(len(data))]
    return list_links


def make_list_title(data):
    #id_youtube = data[0]["titre"]
    list_links = [data[i]["titre"] for i in range(len(data))]
    return list_links


@app.route('/', methods=['GET'])
def index():
    data_azure = db.select("AZURE")
    data_sre = db.select("SRE")
    data_python = db.select("PYTHON")
    #link_youtube = data_azure[0]["link"]
    azure_videos = make_list(data_azure) + \
        make_list(data_sre) + make_list(data_python)
    my_titles = make_list_title(
        data_azure) + make_list_title(data_sre) + make_list_title(data_python)
    # Script qui recupere cours
    # return json.dumps(liste_links)
    my_count = 1
    return render_template("main.html", all_videos=azure_videos, all_title=my_titles, count_test=my_count)


@app.route('/', methods=['POST'])
def search_bar():
    my_research = request.form.get('search_bar_item')
    print("my research :", my_research)
    link_search = db.select_from_tag(my_research)
    link_search_clean = []
    for i in range(len(link_search)):
        link_search_clean.append(link_search[i]['link'])
    link_template = list(make_list_from_link(link_search_clean))
    return render_template("search.html", all_videos=link_template, search_element=my_research)


@app.route('/cours/<name>')
# This will  serve and fetch all cours in /cours/python  /azure /sre / etc..
def view_individual_cours(name):
    data_cours = db.select(name.upper())
    video_links = make_list(data_cours)
    print(video_links)
    # Script qui recupere cours
    return render_template("cours.html", data=video_links, name=name)

# Retourne un formulaire


@app.route('/insert-playlist', methods=['GET'])
def playlist_panel():
    return render_template("insert-cours.html")

# Route pour ajouter des videos a la base de données


@app.route('/insert', methods=['GET'])
def layout():
    # hard coded ---> on doit reprendre ça en dynamique
    cours = ['AZURE', 'SRE', 'PYTHON']
    return render_template("insert-video.html", cours=cours)


@app.route('/insert-video', methods=['POST', 'GET'])
def insert_playlist():
    nom_cours = request.form['cours']
    link_cours = request.form['link']
    level = request.form['niveau']
    title = request.form['title']
    description = request.form['descrip']
    tags = request.form['tags']
    # Le rate ou ponctuation d'un video commence a zero
    rate = "0"
    new_video_info = [link_cours, level, title, description, tags, rate]
    # return json.dumps(new_video_info)
    print(nom_cours)
    print(new_video_info)
    q = db.add_new_video(nom_cours, new_video_info)
    return json.dumps(db.select(nom_cours))
    # return q
# @app.errorhandler(Exception)
# def server_error(err):
#    return render_template('notfound.html'), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
