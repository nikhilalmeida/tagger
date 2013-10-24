import sqlite3

from selftag import app
from config import tagger_root

from contextlib import closing
from os.path import join
from flask import g

image_urls = ['http://s5.tinypic.com/ny8hf7_th.jpg', 'http://s5.tinypic.com/1111845_th.jpg', 'http://s5.tinypic.com/111188w_th.jpg']
image_titles = ['Test', 'Test1', 'Test2']
image_tags = ['Up, Old Man', 'Good, Looking', 'Hi, Hello']
image_values = zip(image_urls, image_titles, image_tags)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    schema_file = join(tagger_root, 'schema.sql')
    with closing(connect_db()) as db:
        with app.open_resource(schema_file, 'r') as out:
            db.cursor().executescript(out.read())
        db.commit()


def insert_images():
    sql = 'INSERT INTO images VALUES (?, ?, ?)'
    conn = connect_db()
    cursor = conn.cursor()
    cursor.executemany(sql, image_values)
    conn.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
