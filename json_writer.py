import requests
import json
import csv

def write_json(url, file_path):

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        pretty_json = json.dumps(data, indent=4)
        with open(file_path, "w") as file:
            file.write(pretty_json)

if __name__ == "__main__":
    url = "https://fantasy.premierleague.com/api/element-summary/355/" #adjust as needed
    file_path = "element-summary.json"
    write_json(url, file_path)