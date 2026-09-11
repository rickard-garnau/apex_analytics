import pandas as pd
import dlt
from pathlib import Path
import os

@dlt.resource(write_disposition="replace")
def load_csv_resource(file_path: str, **kwargs):
    df = pd.read_csv(file_path, **kwargs)
    yield df

if __name__ == "__main__":
    working_directory = Path(__file__).parent
    csv_path = working_directory.parent / "data" / "country_codes.csv"
    data = load_csv_resource(csv_path, encoding="latin1")
    print(data)
    pipeline = dlt.pipeline(
        pipeline_name='apex_analytics',
        destination="snowflake",
        dataset_name='staging'
    )

    load_info = pipeline.run(data, table_name="country_codes")

    print(load_info)