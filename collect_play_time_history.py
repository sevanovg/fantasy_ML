import collections
import statistics
import requests
import json
import csv

def getMinutesDataForLearning():

    url = "https://fantasy.premierleague.com/api/bootstrap-static/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        play_time_hist = []
        players = data['elements']
        for player in players:
            player_id = player['id']

            #get the element summary json for the player
            player_url = "https://fantasy.premierleague.com/api/element-summary/" + str(player_id) + "/"
            response = requests.get(player_url)
            data = response.json()

            #get the game history
            player_history = data['history']

            #create rows of data for learning
            minutes_deque = collections.deque()
            for idx, hist in enumerate(player_history):
                
                #create a row for learninig
                if len(minutes_deque) == 4:
                    #get the average minutes of previous games
                    avg_minutes = sum(minutes_deque) / len(minutes_deque)

                    #get the median minutes of previous games
                    median_minutes = statistics.median(minutes_deque)

                    # #create a row of data
                    # data_row = [player['first_name'], #first name
                    #             hist['round'], #round number
                    #             minutes_deque[-1], #previous game minues
                    #             avg_minutes, #avg minutes for X previous games
                    #             median_minutes, #median minutes for X previous games
                    #             hist['minutes'],] #actual minutes for the game
                    
                    #create a row of data
                    data_row = [player['first_name'], #first name
                                hist['round'], #round number
                                minutes_deque[-1], #previous game minues
                                minutes_deque[-2],
                                minutes_deque[-3],
                                minutes_deque[-4],
                                hist['minutes'],] #actual minutes for the game

                    #add the row
                    play_time_hist.append(data_row)

                #update the deque
                if len(minutes_deque) == 4:
                    minutes_deque.pop()
                minutes_deque.appendleft(hist['minutes'])
        
        writeToCsv('minutes_learning.csv', play_time_hist)

def writeToCsv(name, data):
        csv_file = name

        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)

    
if __name__ == "__main__":
    getMinutesDataForLearning()

