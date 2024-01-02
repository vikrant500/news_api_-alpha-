import requests

# Enter the API key first
def get_news(topic, from_date, to_date, language = 'en', api_key = 'a'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'

    r = requests.get(url)

    content = r.jso()
    articles = content['articles']
    results = []

    for article in articles:
        results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")

    return results

print(get_news(topic='space', from_date='2022-11-25', to_date='2022-11-28'))


# To Do: make a way to save the data in a .csv file or a word document. Make a webpage for the same aswell