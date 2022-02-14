import feedparser

"""
RSS feeds parser based on feedparser

Reads feeds url in a specified file input_file and writes selected elements to ouput_file
"""

inputFile = "/home/tom/Developpement/Git/Alphabeta/Rss_parser/rss_feeds_urls.txt"
outputFile = "/home/tom/Developpement/Git/Alphabeta/Rss_parser/rss_resume.txt"

with open(inputFile, mode = "r") as inFile:
    
    urls = []

    for feedUrl in inFile:
        if feedUrl[0] != "#":
            urls.append(feedUrl)
    
print(urls)

with open(outputFile, mode = "w") as outFile:

    for url in urls :

        feed = feedparser.parse(url)
        for entry in feed.entries:
            # Titre
            outFile.write("[" + entry.published + "] " + entry.title +"\n")
            print(entry.title)
        # Date de publication
            #outFile.write(entry.published)
            print(entry.published)
        # Permalink
        # link = entry.link
        # print(link)
        # # Description sommaire
        # summary = entry.summary
        # print(summary)
        # # Le contenu HTML
        # content = entry.content
        # #print(content)
        # print('')




# url = "https://korben.info/feed"

# feed = feedparser.parse(url)