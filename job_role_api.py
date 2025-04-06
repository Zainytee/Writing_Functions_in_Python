# import libary
import pandas as pd
import requests

# Task 1
job_api_url = "https://jobicy.com/api/v2/remote-jobs?" \
               "count=20&" \
               "geo=usa&" \
               "industry=marketing&" \
               "tag=seo"


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
        return None
    return api_data


# Checking the extracted data
job_dict = get_results(job_api_url)


df_job = pd.DataFrame(job_dict)

all_jobs = job_dict['jobs']

# Extracting all seniors and manager titles into a separate the all_job dict
senior_role = []
manager_role = []
for job in all_jobs:
    if 'senior' in job['jobTitle'].lower():
        senior_role.append(job['jobTitle'])
    elif 'manager' in job['jobTitle'].lower():
        manager_role.append(job['jobTitle'])
print(senior_role)
print(manager_role)
