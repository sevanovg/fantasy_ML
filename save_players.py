import requests
import json
import csv

url = "https://fantasy.premierleague.com/api/bootstrap-static/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    players = data['elements']
    
    output = []
    output.append(players[0].keys()) #header
    for player in players:
        output.append(list(player.values()))
    
    csv_file = "data.csv"

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in output:
            writer.writerow(row)

    # pretty_json = json.dumps(data, indent=4)
    # file_path = "output.json"
    # with open(file_path, "w") as file:
    #     file.write(pretty_json)