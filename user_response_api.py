import requests
import pandas as pd

response_url = "https://randomuser.me/api/?results=500"


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

user_response = get_results(response_url)
user_results=user_response['results']

df_response = pd.DataFrame(user_results)

print(df_response.head())

#Extracting all male and female profile into a separate list
female_profile = []
male_profile = []
for users in user_results:
    if users['gender'] == 'female':
        female_profile.append(users)
    elif users['gender'] == 'male':
        male_profile.append(users)
print(female_profile)
print(male_profile)

#Extracting date part of the date of birth into another list
dob =[]
for users in user_results:
    dob.append(users['dob']['date'])
print(dob)

#Extracting the concatenated full name into another list
full_name= []
for users in user_results:
    full_name.append(users['name']['first']+ ' '+ users['name']['last'])
print(full_name)