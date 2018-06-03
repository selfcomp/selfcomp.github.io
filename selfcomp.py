from flask import Flask, render_template

app = Flask(__name__)

import os, re
scwiki_path = '/home/renato/.vim/pack/prv/opt/wiki/aux/wiki/selfcomp/'
files = os.listdir(scwiki_path)
files = [i for i in files if 'html' not in i]
df = {}
for f in files:
    f_ = scwiki_path + f
    if os.path.isfile(f_):
        ff = open(f_).readlines()
        ff = [i.replace("\n", '') for i in ff]
        ff = [re.sub(r"(./[a-zA-Z/]*)", r'<a href="\1">\1</a>', i) for i in ff]
        df[f]=ff


@app.route("/")
def index():
    return render_template('index.html', title='selfcomp, auto-compilations directory', lines=df['index'])

# @app.route("/about/")
# def index():
#     return render_template('about.html')
# 
# @app.route("/notes/")
# def index():
#     return render_template('notes.html')
# 
# @app.route("/readme/")
# def index():
#     return render_template('readme.html')
# 
# @app.route("/collections/")
# def index():
#     return render_template('collections.html')
# 
# @app.route("/screencast/")
# def index():
#     return render_template('screencast.html')
# 
# @app.route("/releases/")
# def index():
#     return render_template('releases.html')
# 
# @app.route("/rec/<person>")
# def rec():
#     return render_template('rec.html')
# 
# @app.route("/rel/<int:release>")
# def rel():
#     return render_template('rel.html')




