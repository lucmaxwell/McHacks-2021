from newspaper import Article
import sqlite3
import newspaper

keyword="Dalhousie"

#Connect to the sqlite database
conn = sqlite3.connect('articlesdb.sqlite')


cur = conn.cursor()
cur.execute("SELECT id FROM article WHERE title LIKE '%?%'", (keyword))