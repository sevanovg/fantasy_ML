import requests
import json


url = "https://fantasy.premierleague.com/api/bootstrap-static/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    #get the list of all upcoming gameweeks
    upcoming_events = [] #ids of upcoming gameweeks
    events = data['events']
    for event in events:
        if not event['finished']:
            id = event['id']
            upcoming_events.append(id)

    players = data['elements']
    for player in players:

        #load saved json for a player
        player_id = player['id']
        player_json_path = "player_stats/" + str(player_id) + ".json"
        with open(player_json_path, 'r') as file:
            player_data = json.load(file)
        
        #create a row of data
        prediction_row = [player_id]




