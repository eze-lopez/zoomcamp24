import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API

    Example TARGET_URL:
    'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz'
    'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'
    """
    base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_trip_data_2020-'

    target_months = [10,11,12]

    taxi_dtypes = {
        "VendorID": pd.Int64Dtype(),
        "lpep_pickup_datetime": pd.Int64Dtype(),
        "lpep_dropoff_datetime": pd.Int64Dtype(),
        "store_and_fwd_flag": str,
        "RatecodeID": pd.Int64Dtype(),
        "PULocationID": pd.Int64Dtype(),
        "DOLocationID": pd.Int64Dtype(),
        "passenger_count": pd.Int64Dtype(),
        "trip_distance": float,
        "fare_amount": float,
        "extra": float,
        "mta_tax": float,
        "tip_amount": float,
        "tolls_amount": float,
        "ehail_fee": float,
        "improvement_surcharge": float,
        "total_amount": float,
        "payment_type": float,
        "trip_type": float,
        "congestion_surcharge": float,
    }

    #date_fields = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]

    final_df = pd.DataFrame()

    target_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz"
    df = pd.read_csv(target_url, sep=",", compression="gzip", dtype=taxi_dtypes)#, parse_dates= date_fields)

    return df
    # for month in target_months:
    #     target_url = base_url + str(month) + ".csv.gz"
    #     print(target_url)

    #     df = pd.read_csv(target_url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates= date_fields)
    #     df["lpep_pickup_date "] = df["lpep_pickup_datetime"].dt.date

    #     print(df["lpep_pickup_date"].head())



    # return pd.read_csv(url, sep=",", compression="gzip",dtype=taxi_dtypes, parse_dates= date_fields)
