import urllib.request
import json
import urllib.parse

def search_wikipedia(query):
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&utf8=&format=json"
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        for item in data['query']['search'][:5]:
            print(f"Title: {item['title']}\nSnippet: {item['snippet']}\n")
    except Exception as e:
        print(e)

search_wikipedia("Middletown Connecticut geology")
search_wikipedia("Middletown Connecticut environment")
search_wikipedia("Connecticut River valley geology")
