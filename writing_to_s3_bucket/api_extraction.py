import pandas as pd
import boto3
import awswrangler as wr
import os
import requests
from dotenv import load_dotenv


#Football API

football_url = "http://api.football-data.org/v4/competitions/"
football_response = requests.get(football_url)
print(football_response.status_code)

football_response=football_response.json()
football_response.keys()
df = pd.json_normalize(football_response)

access_key = os.getenv("acess_key")
secret_key = os.getenv("secret_key")
region = os.getenv("region")


session = boto3.session.Session(
    aws_access_key_id = "acess_key",
    aws_secret_access_key = "secret_key",
    region_name = "region"
)

wr.s3.to_parquet(
    df=df,
    path="s3://zainab-ojo-data-bucket/football_respose_data/",
    boto3_session=session,
    mode="append",
    dataset=True
)


#Guardian API
api_url = "https://content.guardianapis.com/search?q=Nigeria&from-date=2025-01-01&api-key=test"

api_niga = requests.get(api_url)

print(api_niga.status_code)

niga_article = api_niga.json()

df_guard = pd.json_normalize(niga_article)

wr.s3.to_parquet(
    df=df_guard,
    path="s3://zainab-ojo-data-bucket/guardian_respose_data/",
    boto3_session=session,
    mode="append",
    dataset=True
)


#Job API

job_url = "https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo"
job_response = requests.get(job_url)
job_dict = job_response.json()

df_job = pd.json_normalize(job_dict)