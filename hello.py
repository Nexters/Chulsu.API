from flask import Flask
from flask import request
from models import Info
from database import init_db
from database import db_session
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route("/save",methods=['POST'])
def save():
    print(request.values["desc"])
    i = Info(request.form["text"], request.form["desc"],request.form["etc"])
    db_session.add(i)
    db_session.commit()
    return "joonhoi"

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/list')
def show_entries():
  infos_query = db_session.query(Info)
  infos = [dict(text=info.text, description=info.description, etc=info.etc, created_at=info.created_at) for info in infos_query]

  print infos

  return render_template('show_infos.html', infos=infos)


if __name__ == "__main__":
    init_db()
    app.run(port=4200)
