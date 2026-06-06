import sqlite3

DB_NAME = 'social_network.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_posts():
    """Bütün postları bazadan ən son paylaşılandan başlayaraq çəkir"""
    with get_db_connection() as conn:
        posts = conn.execute('SELECT * FROM user_posts ORDER BY id DESC').fetchall()
    return posts

def insert_new_post(author, message):
    """Yeni postu bazaya daxil edir"""
    with get_db_connection() as conn:
        conn.execute('INSERT INTO user_posts (author, message) VALUES (?, ?)', (author, message))
        conn.commit()
