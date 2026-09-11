import requests
import json

url = "https://api.jolpi.ca/ergast/f1/2026/races.json"

def _get_races():
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def number_of_races():
    json_response = _get_races()
    number_of_races = json_response['MRData']['total']
    print(f"\nNumber of races = {number_of_races}")

if __name__ == '__main__':
    number_of_races()