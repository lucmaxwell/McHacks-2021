import newspaper
sites = ["https://cbc.ca/","https://www.cnn.com/","https://news.ycombinator.com/","https://globalgoodness.ca/en/"]
# sites to get news from

contentUrl = []  # empty array to store all the links

for i in range(len(sites)):     # nested for loop to append all the links to the contentUrl
    site = newspaper.build(sites[i], memoize_articles=False)
    urls = site.article_urls()
    for j in range(len(urls)):
        contentUrl.append(urls[i])


