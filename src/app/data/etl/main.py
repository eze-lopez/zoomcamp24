import argparse
import os
from io import StringIO

import pandas as pd
import requests
import wget
from dotenv import load_dotenv
from sqlalchemy import create_engine

parser = argparse.ArgumentParser()

parser.add_argument(
    "--date", help="Date for dataset. Format accepted 'yyyy-mm-dd'.", required=True
)
parser.add_argument(
    "--taxi-color", help="Taxi color. Could be yellow or green.", required=True
)

args = parser.parse_args()

params = vars(args)
print(f"Running ETL with params: {params}")


def download_with_requests(url: str):
    r = requests.get(url)
    df = pd.read_csv(StringIO(r.text))
    df.to_parquet(".docker_volumes/downloads/zone.parquet", engine="fastparquet")


def download_with_wget(url: str):
    wget.download(
        url,
        f".docker_volumes/downloads/{params.get('taxi_color')}_taxi_{params.get('date')[:7]}.parquet",
    )


if __name__ == "__main__":
    load_dotenv()
    TAXI_URL = os.getenv("NYC_TAXI_URL", "NULL. Not load properly.")
    ZONE_URL = os.getenv("NYC_ZONE_URL", "NULL. Not load properly.")

    # url_example taxi yellow "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-07.parquet"
    TAXI_TARGET_URL = (
        TAXI_URL
        + f"{params.get('taxi_color')}_tripdata_{params.get('date')[:7]}.parquet"
    )

    print("-" * 10 + "\nTARGETS:\n")
    print(f"TAXI URL: {TAXI_TARGET_URL}")
    print(f"ZONE URL: {ZONE_URL}")

    print("-" * 10 + "\nDOWNLOADING DATA...\n")
    taxi_file = download_with_wget(TAXI_TARGET_URL)
    zone_file = download_with_requests(ZONE_URL)

    print()
    print("-" * 10 + "\nINSERTING DATA...\n")

    # db_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:{os.getenv('POSTGRES_CONTAINER_PORT')}/{os.getenv('POSTGRES_DB')}"
    db_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:{os.getenv('POSTGRES_CONTAINER_PORT')}/{os.getenv('POSTGRES_DB')}"
    engine = create_engine(db_url)

    df_trips = pd.read_parquet(
        f".docker_volumes/downloads/{params.get('taxi_color')}_taxi_{params.get('date')[:7]}.parquet",
        "fastparquet",
    )
    # print(pd.io.sql.get_schema(df_trips, name="green_taxi_data", con=engine))
    df_trips.to_sql(
        name=f"{params.get('taxi_color')}_taxi_data",
        con=engine,
        if_exists="replace",
        index=False,
    )

    df_zones = pd.read_parquet(
        ".docker_volumes/downloads/zone.parquet",
        "fastparquet",
    )
    # print(pd.io.sql.get_schema(df_zones, name="green_taxi_data", con=engine))
    df_zones.to_sql(
        name="zones",
        con=engine,
        if_exists="replace",
        index=False,
    )

    print("ETL ends successfully.")
