import dlt
import requests
import json
import httpx

url = "https://api.jolpi.ca/ergast/f1/2026/races.json"

def get_races():
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()

@dlt.resource(write_disposition="replace")
def view_races():
    json_response = get_races()
    races = json_response['MRData']['RaceTable']['Races']
    for race in races:
        yield race

def run_pipeline(view_races): 
    pipeline = dlt.pipeline(
        pipeline_name ="apex_analytics",
        destination="snowflake",
        dataset_name="staging"
    )

    load_races = pipeline.run(view_races)
    print(load_races)



if __name__ == '__main__':
    run_pipeline(view_races)

