import requests

# Enter the API key first
def get_news(country, api_key = 'c246af9bc54b48daabbc30093873c27a'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'

    r = requests.get(url)

    content = r.json()
    articles = content['articles']
    results = []

    for article in articles:
        results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")

    return results

print(get_news(country='us'))


# To Do: make a way to save the data in a .csv file or a word document. Make a webpage for the same aswell