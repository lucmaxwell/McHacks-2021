from newspaper import Article
import sqlite3

#URL List to scrape articles from
url_list = ['https://www.cbc.ca/news/canada/alternative-lenders-marketplace-1.5891676','https://www.cbc.ca/news/world/india-farmers-hunger-strike-1.5894769']

#Create the sqlite database:
conn = sqlite3.connect('/Users/fredericmheir/Documents/mchacks8/McHacks-2021/articlesdb.sqlite')

cur = conn.cursor()
sql_command = """
    DROP TABLE IF EXISTS article;
    CREATE TABLE article (url VARCHAR, title VARCHAR, content VARCHAR);
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
    

    print("title: "+article_title+", url: "+article_url)
    
conn.close()
