import os
import sys

import awswrangler as wr
import boto3
from football_api import df_football
from guardian_api import df_guard
from job_role_api import df_job
from user_response_api import df_response

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEYy")
REGION = os.getenv("REGION")


session = boto3.session.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION
)

# Writing Football API to s3 Bucket
wr.s3.to_parquet(
    df=df_football,
    path="s3://zainab-ojo-data-bucket/football_respose_data/",
    boto3_session=session,
    mode="append",
    dataset=True
)

# Writing Guardian API to s3 Bucket
wr.s3.to_parquet(
    df=df_guard,
    path="s3://zainab-ojo-data-bucket/guardian_respose_data/",
    boto3_session=session,
    mode="append",
    dataset=True
)


# Writing User_Response API to s3 Bucket
wr.s3.to_parquet(
    df=df_response,
    path="s3://zainab-ojo-data-bucket/user_respose_data/",
    boto3_session=session,
    mode="append",
    dataset=True
)

# Writing Job_Response API to s3 Bucket
wr.s3.to_parquet(
    df=df_job,
    path="s3://zainab-ojo-data-bucket/job_respose_data/",
    boto3_session=session,
    mode="append",
    dataset=True
)
