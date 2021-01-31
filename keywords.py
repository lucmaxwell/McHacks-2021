from newspaper import Article
import sqlite3
import newspaper

keyword_list=["good", "happy", "feeling", "beautiful", "cheerful", "delightful", "funny", "excited"]

#Connect to the sqlite database
conn = sqlite3.connect('articlesdb.sqlite')
cur = conn.cursor()

#For identify articles (by ID) that contain the keywords.
for keyword in keyword_list:
    cur.execute("SELECT id FROM article WHERE content LIKE '%{site}%'".\
        format(site = keyword))

matched_id = cur.fetchall()

conn.commit()

#Below : To extract content from SQL associated with matched_id
cur = conn.cursor()

matched_titles=[]

for id in matched_id:
    cur.execute("SELECT title FROM article WHERE id={ids};".\
        format(ids=id[0]))
    matched_titles.append(cur.fetchall())

conn.commit()

conn.close()

print(matched_titles)
