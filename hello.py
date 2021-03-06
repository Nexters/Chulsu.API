# -*- coding:utf-8 -*-
import argparse, daemon, os
from flask import Flask
from flask import request
from models import Info
from database import init_db
from database import db_session
from sqlalchemy import desc
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

"""
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
"""

@app.route("/save",methods=['POST'])
def save():
    i = Info(request.form["text"], request.form["desc"],request.form["etc"])
    db_session.add(i)
    db_session.commit()
    return "joonhoi"

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/list/<int:page>')
def show_entries(page):
    page = page - 1
    page_cnt = 20
    infos_query = db_session.query(Info).order_by(desc(Info.id)).limit(page_cnt).offset(page_cnt*page)
    count = (db_session.query(Info).count() / page_cnt ) + 1

    infos = [dict(text=info.text, description=info.description, etc=info.etc, created_at=info.created_at) for info in infos_query]
    print count
    return render_template('show_infos.html', count=count, infos=infos)

def main():
    init_db()
    app.run(host='0.0.0.0', port=3002)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--daemon', action='store_true', default=False, help='Run as daemon')
    arg_parser.add_argument('--cwd', action='store', default='/',
                            help='Full path of the working directory to which the process should change on daemon start.')
    arg_parser.add_argument('--uid', action='store', type=int, default=os.getuid(),
        help='The user ID ("UID") value and group ID ("GID") value to switch the process to on daemon start.')
    args = vars(arg_parser.parse_args())

    if args['daemon']:
        context = daemon.DaemonContext(working_directory=args['cwd'], uid=args['uid'])
        with context:
            main()
    else:
        main()

