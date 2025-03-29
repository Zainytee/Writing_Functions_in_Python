import requests
import pandas as pd


api_url = "https://content.guardianapis.com/search?q=Nigeria&from-date=2025-01-01&api-key=test"


api_niga = requests.get(api_url)

print(api_niga.status_code)

niga_article = api_niga.json()

article_response = niga_article['response']['results']

pagenum = niga_article['response']['pages']


def get_results():
    """
    result: return all the data in each of the pages and append the result into the empty.

    """
    nigeria_articles = []
    for i in range(1,pagenum+1):
        for elements in article_response:
            nigeria_articles.append(elements)
    return nigeria_articles

results = get_results()

df = pd.DataFrame(results)

print(df.head())

df.to_csv('nigeria_articles.csv')