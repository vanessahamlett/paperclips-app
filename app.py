from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z_beep_beep_boop_boop'

# sqlite_uri = 'sqlite:///' + os.path.abspath(os.path.curdir) + '/paperclips.db'
if 'DB_PATH' not in os.environ:
    print('DB_PATH must be set')
    exit(1)
sqlite_uri = 'sqlite:///' + os.environ['DB_PATH'] + '/paperclips.db'
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Paperclip
import random
import string

def randstr():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

@app.before_first_request
def init():
    try:
        Paperclip.query.all()
    except:
        db.create_all()

@app.route('/')
def index():
    return redirect(url_for('show_paperclips'))

@app.route('/make-paperclip/')
def make_paperclip():
    p = Paperclip(serialnum=randstr())
    db.session.add(p)
    db.session.commit()
    return p.serialnum

@app.route('/paperclips/')
def show_paperclips():
    ps = Paperclip.query.all()
    for i in range(0, len(ps)):
        ps[i] = ps[i].serialnum
    return str(ps)

