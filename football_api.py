import pandas as pd
import requests

football_url = "http://api.football-data.org/v4/competitions/"


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


football_response = get_results(football_url)

df_football = pd.json_normalize(football_response)

df_football.head()

# Extracting all competiton information in the data
football_competition = football_response['competitions']

# Extracting competiton name from the football_competiton dict created
competiton_name = []
for competition in football_competition:
    competiton_name.append(competition['name'])
print(competiton_name)
