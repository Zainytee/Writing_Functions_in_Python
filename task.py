import requests
import json



api_url = "https://content.guardianapis.com/search?q=Nigeria&from-date=2025-01-01&api-key=test"


testing = requests.get(api_url)

params={
    q='Nigeria',
    from_date='2025-01-01',
    api_key='api_key',
    page_size=50
}

