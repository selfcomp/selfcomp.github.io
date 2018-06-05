from flask import Flask, render_template

app = Flask(__name__)

import os, re
scwiki_path = './static/wiki/'
files = os.listdir(scwiki_path)
files = [i for i in files if 'html' not in i]
files = [i for i in files if not i.endswith('.swp')]

recwiki_path = scwiki_path + '/rec'
files_ = os.listdir(recwiki_path)
files_ = ['rec/'+i for i in files_ if 'html' not in i]
files_ = [i for i in files_ if not i.endswith('.swp')]

files += files_

relwiki_path = scwiki_path + '/rel'
files_ = os.listdir(relwiki_path)
files_ = ['rel/'+i for i in files_ if 'html' not in i]
files_ = [i for i in files_ if not i.endswith('.swp')]

files += files_

df = {}
for f in files:
    f_ = scwiki_path + f
    if os.path.isfile(f_):
        ff = open(f_, encoding='utf-8').readlines()
        ff = [i.replace("\n", '') for i in ff]
        ff = [re.sub(r"(:.+:)", r'<span class="Error">\1</span>', i, flags=re.M) for i in ff]
        ff = [re.sub(r"( [ativos]+[,$])", r'<span class="WarningMsg">\1</span>', i, flags=re.M) for i in ff]
        ff = [re.sub(r"( [hr+]+[,$])", r'<span class="WarningMsg">\1</span>', i, flags=re.M) for i in ff]
        ff = [re.sub(r"\.(/[a-zA-Z/0-9áéíóú]*)", r'<a href="\1/">.\1</a>', i) for i in ff]
        ff = [re.sub(r"(\~+[ ()\-a-zA-Z0-9\./\:]*\~+)", r'<span class="Comment">\1</span>', i) for i in ff]
        df[f]=ff

linenos = ['{: 3d}'.format(i+1) for i in range(999)]


@app.route("/")
def index():
    return render_template('index.html', title='Index', lines=df['index'], ln=linenos)

@app.route("/rf/")
def rf():
    return render_template('index.html', title='me?', lines=df['rf'], ln=linenos)

@app.route("/about/")
def about():
    return render_template('index.html', title='About', lines=df['about'], ln=linenos)

@app.route("/notes/")
def notes():
    return render_template('index.html', title='Notes', lines=df['notes'], ln=linenos)

@app.route("/readme/")
def readme():
    return render_template('index.html', title='Readme', lines=df['readme'], ln=linenos)

@app.route("/screencast/")
def screencast():
    return render_template('index.html', title='Screencast(s)', lines=df['screencast'], ln=linenos)

@app.route("/releases/")
def releases():
    return render_template('index.html', title='Releases', lines=df['releases'], ln=linenos)

@app.route("/collections/")
def collections():
    return render_template('index.html', title='Collections', lines=df['collections'], ln=linenos)

@app.route("/rec/<person>/")
def rec(person):
    return render_template('index.html', title='rec '+person, lines=df['rec/'+person], ln=linenos)
 
@app.route("/rel/<release>/")
def rel(release):
    return render_template('index.html', title='rel '+release, lines=df['rel/'+release], ln=linenos)

