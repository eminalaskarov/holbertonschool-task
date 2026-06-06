import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from models import fetch_all_posts, insert_new_post, DB_NAME

app = Flask(__name__)

def init_db():
    """Əgər baza faylı yoxdursa, schema.sql işə salınır"""
    if not os.path.exists(DB_NAME):
        with sqlite3.connect(DB_NAME) as conn:
            with open('schema.sql', 'r') as f:
                conn.executescript(f.read())

init_db()

@app.route('/')
def home():
    feed_posts = fetch_all_posts()
    return render_template('index.html', posts=feed_posts)

@app.route('/publish', methods=['POST'])
def publish_post():
    username = request.form.get('username')
    content = request.form.get('content')
    
    if username and content:
        insert_new_post(username, content)
        
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
