import collections
import statistics
import requests
import json
import csv
from json_writer import write_json

def dump_player_history_json():

    url = "https://fantasy.premierleague.com/api/bootstrap-static/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        players = data['elements']
        for player in players:
            player_id = player['id']

            #dump json file for each player's history
            player_url = "https://fantasy.premierleague.com/api/element-summary/" + str(player_id) + "/"
            path = "player_history/" + str(player_id) + ".json"
            write_json(player_url, path)
    
if __name__ == "__main__":
    dump_player_history_json()

