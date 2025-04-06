import requests
import pandas as pd
api_url = "https://content.guardianapis.com/search?q=Nigeria&from-date=2025-01-01&api-key=test"


def get_results(api_url):
    """
    A generic function that retrieve data from a given API
    Args:
        An APi URL
    Returns:
    API data in json format

    """
    api_info = requests.get(api_url)
    if api_info.status_code == 200:
        api_data = api_info.json()
    else:
        print("Error in fetching data from the API provided")
    return api_data

nga_article = get_results(api_url)


article_response = nga_article['response']['results']

pagenum = nga_article['response']['pages']

nigeria_articles = []
for i in range(1, pagenum+1):
    for elements in article_response:
        nigeria_articles.append(elements)
# df_guard = pd.json_normalize(niga_article)
df_guard = pd.DataFrame(nigeria_articles)

print(df_guard.head())
# df.to_csv('nigeria_articles.csv')
