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
matched_content=[]
matched_url=[]

for id in matched_id:
    cur.execute("SELECT title FROM article WHERE id={ids};".\
        format(ids=id[0]))
    matched_titles.append(cur.fetchall())

conn.commit()

for id in matched_id:
    cur.execute("SELECT content FROM article WHERE id={ids};".\
        format(ids=id[0]))
    matched_content.append(cur.fetchall())
conn.commit()

for id in matched_id:
    cur.execute("SELECT url FROM article WHERE id={ids};".\
        format(ids=id[0]))
    matched_url.append(cur.fetchall())
conn.commit()

conn.close()

file = open("data.txt", "w", encoding = 'UTF-8')
file.write("")
for i in range(len(matched_titles)):
    currContent = matched_content[i][0][0].split("\n")[0] + "..."
    file.write(matched_titles[i][0][0] + "\n" + currContent + "\n" + matched_url[i][0][0] + "\n")
file.close()