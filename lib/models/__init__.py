import sqlite3

CONN = sqlite3.connect('reviews.db')
CURSOR = CONN.cursor()