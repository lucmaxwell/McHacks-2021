from newspaper import Article
import sqlite3
import newspaper

sites = ["https://cbc.ca/","https://www.cnn.com/","https://news.ycombinator.com/","https://globalgoodness.ca/en/"]
# sites to get news from

contentUrl = []  # empty array to store all the links

for i in range(len(sites)):     # nested for loop to append all the links to the contentUrl
    site = newspaper.build(sites[i], memoize_articles=False)
    urls = site.article_urls()
    for j in range(len(urls)):
        contentUrl.append(urls[i])
#URL List to scrape articles from
url_list = contentUrl

#Create the sqlite database:
conn = sqlite3.connect('articlesdb.sqlite')

cur = conn.cursor()
sql_command = """
    DROP TABLE IF EXISTS article;
    CREATE TABLE article (id INTEGER PRIMARY KEY AUTOINCREMENT,url VARCHAR, title VARCHAR, content VARCHAR);
"""
cur.executescript(sql_command)
conn.commit()

#For each article in the database, scrape the article, then insert the title, content and url in the sqlite database created.
for url in url_list:
    article = Article(url)

    article.download()

    article.parse()

    article_text = article.text
    article_title = article.title
    article_url = url
    
    cur.execute("INSERT INTO article (url, title, content) VALUES (?,?,?);", (article_url, article_title, article_text))
    conn.commit()
    

    print(f"title: {article_title}, url: {article_url}")
    
    
conn.close()
