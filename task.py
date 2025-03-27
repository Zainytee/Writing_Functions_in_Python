import requests
import time
import pandas as pd
def request(data):
    '''
    Sends a request to an API using the requests module.
    Args: 
        string:base url.
    Returns:
        dict: A paginated response in JSON format.
    '''
    for i in range(500): # range to detemine the number of request iteration on the api
        response = requests.get(data)
        res = response.status_code
        if res == 200:
            file = response.json()
            print(f'requesting page {i+1} from the base url')
        time.sleep(2)  # this allows 2 seconds before the next iteration, requirement is at least 1 second
        yield file
def extract(base_url):
    '''
    extracts from an inner api request function, converts to dataframe and export into a csv

    Args:
        yield value from the inner request function

    Returns:
        csv formatted file
    '''
    extracted_file =[] 
    raw_data= [] 
    for i in request(base_url):
        row = {} #initialized a dict to take in the output of the yield in the request function
        row['new1']= i
        raw_data.append(row)
    print(f'extracting a total of {len(raw_data)} pages from the base_url')
    for new in raw_data:
        article = new['new1']['response']['results']
        for details in article:
            extracted_file.append(details)
    df =pd.DataFrame(extracted_file)
    print(f'data completely processed and about to be inserted in a csv file')
    df.to_csv('api_doc2.csv')
    print(f'data successfully processed and downloaded to api_doc file')
    return df
   
