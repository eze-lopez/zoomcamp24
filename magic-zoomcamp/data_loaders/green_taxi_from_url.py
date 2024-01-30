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
    """
    target_months = [10,11,12]

    taxi_dtypes = {
        "VendorID": pd.Int64Dtype(),
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

    date_fields = ["lpep_pickup_datetime", "lpep_dropoff_datetime"]

    final_df = pd.DataFrame()
    for month in target_months:
        url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month}.csv.gz"
        response = requests.get(url)
        s = requests.get(url).content

        df = pd.read_csv(
            io.BytesIO(s),
            sep=",",
            compression='gzip',
            parse_dates = date_fields,
            dtype = taxi_dtypes
        )

        final_df = pd.concat([final_df, df])

    return final_df
