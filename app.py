from flask import Flask
from flask import jsonify
from flask import request
from newspaper import Article
import sqlite3
import newspaper
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
        
    #This script will scrape news from the 2 websites below.
    sites = ["https://cbc.ca/", "https://globalgoodness.ca/en/", "https://www.nytimes.com/ca/","https://www.bbc.com/news/world/us_and_canada","https://montrealgazette.com"]

    contentUrl = []  # empty array to store all the links

    for i in range(len(sites)):     # nested for loop to append all the links to the contentUrl
        site = newspaper.build(sites[i], memoize_articles=False)
        urls = site.article_urls()
        for j in range(len(urls)):
            if not any(re.sub(r'^.+/([^/]+)$', r'\1', urls[j]) in word for word in contentUrl):
                contentUrl.append(urls[j])

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
        try: 
            article = Article(url)

            article.download()

            article.parse()

            article_text = article.text
            article_title = article.title
            article_url = url
            
            cur.execute("INSERT INTO article (url, title, content) VALUES (?,?,?);", (article_url, article_title, article_text))
            conn.commit()
        
        except:
            print()
        
    conn.close()

    keyword_list=['achievement', 'admire', 'adorable', 'affirmative', 'amazing', 'angelic', 'appealing', 'attractive', 'awesome', 'beautiful', 'believe', 'beneficial', 'brave', 'bravo', 'brilliant', 'cat', 'celebrated', 'champ', 'champion', 'charming', 'cheery', 'choice', 'commend', 'composed', 'congratulation', 'constant', 'cool', 'courageous', 'creative', 'cute', 'delight', 'delightful', 'distinguished', 'divine', 'dog', 'earnest', 'easy', 'ecstatic', 'effective', 'effervescent', 'efficient', 'effortless', 'electrifying', 'elegant', 'enchanting', 'encouraging', 'endorsed', 'energetic', 'energized', 'engaging', 'enthusiastic', 'essential', 'esteemed', 'ethical', 'excellent', 'exciting', 'exquisite', 'fabulous', 'fantastic', 'favorable', 'fetching', 'fitting', 'flourishing', 'fortunate', 'fresh', 'friendly', 'fun', 'funny', 'generous', 'genius', 'genuine', 'giving', 'glamorous', 'glowing', 'gorgeous', 'graceful', 'great', 'growing', 'handsome', 'happy', 'harmonious', 'healing', 'healthy', 'hearty', 'heavenly', 'honest', 'honorable', 'honored', 'hug', 'ideal', 'imaginative', 'imagine', 'impressive', 'independent', 'innovate', 'innovative', 'intellectual', 'intelligent', 'intuitive', 'inventive', 'jovial', 'joy', 'jubilant', 'kind', 'knowing', 'knowledgeable', 'laugh', 'learned', 'legendary', 'light', 'lively', 'lovely', 'lucid', 'lucky', 'luminous', 'marvelous', 'masterful', 'meaningful', 'merit', 'meritorious', 'miraculous', 'motivating', 'natural', 'nice', 'novel', 'nurturing', 'nutritious', 'optimistic', 'paradise', 'perfect', 'phenomenal', 'pleasant', 'pleasurable', 'positive', 'pretty', 'principled', 'productive', 'prominent', 'protected', 'rejoice', 'reliable', 'remarkable', 'resounding', 'respected', 'restored', 'rewarding', 'robust', 'satisfactory', 'skilled', 'skillful', 'smile', 'soulful', 'sparkling', 'special', 'spirited', 'spiritual', 'stunning', 'successful', 'sunny', 'super', 'superb', 'supporting', 'surprising', 'terrific', 'thrilling', 'thriving', 'tranquil', 'transformative', 'transforming', 'trusting', 'truthful', 'upright', 'upstanding', 'valued', 'vibrant', 'vigorous', 'virtuous', 'vivacious', 'welcome', 'wholesome', 'willing', 'wonderful', 'wondrous', 'worthy', 'wow', 'yummy']

    #Connect to the sqlite database
    conn = sqlite3.connect('articlesdb.sqlite')
    cur = conn.cursor()

    outer_id=[]
    matched_id=[]
    #For identify articles (by ID) that contain the keywords.
    for keyword in keyword_list:
        cur.execute("SELECT id FROM article WHERE content LIKE '%{site}%'".\
            format(site = keyword))
        id_fetched=cur.fetchall()
        outer_id.append(id_fetched)

    for i in outer_id:
        for y in i:
            matched_id.append(y)

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


    for id in matched_id:
        cur.execute("SELECT content FROM article WHERE id={ids};".\
            format(ids=id[0]))
        matched_content.append(cur.fetchall())


    for id in matched_id:
        cur.execute("SELECT url FROM article WHERE id={ids};".\
            format(ids=id[0]))
        matched_url.append(cur.fetchall())

    conn.commit()
    conn.close()
    output = ""
    for i in range(20):
        currContent = matched_content[i][0][0].split("\n")[0] + "..."
        output += matched_titles[i][0][0] + "\n\n\n" + currContent + "\n\n\n" + matched_url[i][0][0] + "\n\n\n\n"

    return jsonify({'message' : output})

if __name__ == "__main__":
    app.run(debug=True)

#End of script