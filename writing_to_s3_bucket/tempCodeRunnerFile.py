import pandas as pd
import boto3
import awswrangler as wr
import os
import sys
import requests
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from guardian_api import df_guard

print(sys.path)

#Football API

football_url = "http://api.football-data.org/v4/competitions/"
football_response = requests.get(football_url)
print(football_response.status_code)

football_response=football_response.json()
football_response.keys()
df = pd.json_normalize(football_response)

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEYy")
REGION = os.getenv("REGION")


session = boto3.session.Session(
    aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = SECRET_KEY,
    region_name = REGION
)

wr.s3.to_parquet(
    df=df,
    path="s3://zainab-ojo-data-bucket/football_respose_data/",
    boto3_session=session,
    mode="append",
    dataset=True
)

"""
#Guardian API
api_url = "https://content.guardianapis.com/search?q=Nigeria&from-date=2025-01-01&api-key=test"

api_niga = requests.get(api_url)

print(api_niga.status_code)

niga_article = api_niga.json()

df_guard = pd.json_normalize(niga_article)

"""
wr.s3.to_parquet(
    df=df_guard,
    path="s3://zainab-ojo-data-bucket/guardian_respose_data/",
    boto3_session=session,
    mode="append",
    dataset=True
)
