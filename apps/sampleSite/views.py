from random import sample
from flask import Blueprint, render_template

sampleSite = Blueprint(
    "sampleSite",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="static/sampleSite"
)
# @hogehoge.route(参�?�url)でそれ以下�?�関数を実行する�?
@sampleSite.route('/')
def index():
    dbData = {
        "id":123,
        "name":"name"
    }
    return render_template("index.html", data=dbData)

@sampleSite.route('/page2')
def page2():
    return render_template("page2.html")

@sampleSite.route('/wiki')
def page3():
    return render_template("wiki.html")

@sampleSite.route('/study')
def page4():
    return render_template("study.html")