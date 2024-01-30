from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

import os
import pyarrow as pa
from pyarrow import parquet as pq

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/src/.secrets/sa-mage.json"
project_id = "zoomcamp24"
bucket_name = "mage-zoomcamp-eze"
table_name = "green_taxi"
root_path = f"{bucket_name}/{table_name}"

@data_exporter
def export_data_to_google_cloud_storage(data: DataFrame, **kwargs) -> None:
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path,
        partition_cols=["lpep_pickup_date"],
        filesystem=gcs
    )
