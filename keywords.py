from newspaper import Article
import sqlite3
import newspaper

keyword="Dalhousie"

#Connect to the sqlite database
conn = sqlite3.connect('articlesdb.sqlite')


cur = conn.cursor()

cur.execute("SELECT url FROM article WHERE content LIKE '%Dalhousie%';")

matched_id = cur.fetchall()

conn.commit()

conn.close()

print(matched_id)