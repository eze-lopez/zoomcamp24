import sys

from src.core.utils.data_download import Downloader

TARGET_URL = (
    "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-09.parquet"
)

params = sys.argv
print(f"Start ETL with params = {params}..")

downloader = Downloader(TARGET_URL)
downloader.download_file()

print("ETL ends successfully.")
