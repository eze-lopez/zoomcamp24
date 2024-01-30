if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data["lpep_pickup_date"] = data["lpep_pickup_datetime"].dt.date

    new_columns = {
        "VendorID":"vendor_id",
        "store_and_fwd_flag":"store_and_fwd_flag",
        "RatecodeID":"rate_code_id",
        "PULocationID":"pu_location_id",
        "DOLocationID":"do_location_id",
        "passenger_count":"passenger_count",
        "trip_distance":"trip_distance",
        "fare_amount":"fare_amount",
        "extra":"extra",
        "mta_tax":"mta_tax",
        "tip_amount":"tip_amount",
        "tolls_amount":"tolls_amount",
        "ehail_fee":"ehail_fee",
        "improvement_surcharge":"improvement_surcharge",
        "total_amount":"total_amount",
        "payment_type":"payment_type",
        "trip_type":"trip_type",
        "congestion_surcharge":"congestion_surcharge",
    }
    # data.columns = data.columns.str.lower()

    data = data.rename(columns=new_columns)

    data = data[data["passenger_count"] > 0]
    data = data[data["trip_distance"] > 0]

    data["lpep_pickup_date"] = data["lpep_pickup_datetime"].dt.date

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    # assert output['vendor_id'].isnull().sum() == 0, "Null vendor_id"
    assert output['passenger_count'].isin([0]).sum() == 0, "There are rides with zero passengers"
    assert output['trip_distance'].isin([0]).sum() == 0, "There are rides with zero trip_distance"
