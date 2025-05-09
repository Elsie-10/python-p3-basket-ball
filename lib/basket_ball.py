def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

game = game_dict()
def num_points_per_game(name):
    
    for team in ["home","away"]:
        for player in game[team]["players"]:
            if player["name"] == name :
                return player["points_per_game"]
    return ("Player not found")

print (num_points_per_game("Rui Hachimura"))

def player_age(name):
    for team in ["home","away"]:
        for player in game[team]["players"] :
            if player["name"] == name :
                return player["age"]
    return ("player not found")
print(player_age("Rui Hachimura"))

def team_colors(team_name):
    for team in ["home", "away"]:
        if game[team]["team_name"] == team_name :
            return game[team]["colors"]
    return ("team_name not found")

print(team_colors("Washington Wizards"))

def team_names():
    names =[]
    for team in ["home","away"]:
        names.append(game[team]["team_name"])
    return names
    
print(team_names())

def player_numbers(team_name):
    jersey_numbers =[]
    for team in ["home", "away"]:
        if game[team]["team_name"] == team_name :
            for player in game[team]["players"] :
                jersey_numbers.append(player["number"])
            return jersey_numbers
    return ("player not found")

print(player_numbers("Cleveland Cavaliers"))

def player_stats(name):
 
    for team in ["home", "away"] :
        for player in game[team]["players"]:
            if player["name"] == name:
               return player
    return("player not found")

print(player_stats("Rui Hachimura"))
            
def average_rebounds_by_shoe_brand () :
    brand_rebounds = {} # sets up an empty dictionary

    for team in ["home", "away"] : # loops through both teams
    # loops through each player on the team
        for player in game[team]["players"]:
    # get the player's brand and rebound per game
            brand = player["shoe_brand"]
            rebounds = player["rebounds_per_game"]
# add the rebound to the correct list in brand_rebounds
            if brand not in brand_rebounds:
                # if the brand is not in the dictionary it creates a new empty list for it
                brand_rebounds[brand] = []
            brand_rebounds[brand].append(rebounds)
# caculate the average for each brand
# takes the sum of rebounds
# divide by the number of players
# round to 2 decimal places
# store the result in a new dictionary called average_by_brand 
    average_by_brand = {}   
    for brand, rebound_list in brand_rebounds.items():
        average=sum(rebound_list) / len(rebound_list)
        average_by_brand[brand] = round(average, 2)
    return average_by_brand
    # returns the final dictionary.
print(average_rebounds_by_shoe_brand())

def most_cereer_points():
    most_cereer_points=0
    top_player = None
    
    for team in ["home", "away"] :
        for player in game[team]["players"]:
            if player["career_points"] > most_cereer_points:
              most_cereer_points = player["career_points"]
              top_player_name = player["name"]
    
    return f"{top_player_name} has {most_cereer_points} career points"

print(most_cereer_points())

def shared_jersey_number():
    home_number = {player["number"] for player in game["home"]["players"]}
    away_number = {player["number"] for player in game["away"]["players"]}

    shared_number = home_number & away_number # set insertion
    return list(shared_number)

print("shared jersey number:", shared_jersey_number())

def player_with_longest_name():
    longest_name= ""

    for team in ["home","away"]:
        for player in game[team]["players"]:
            if len(player["name"]) > len(longest_name):
                longest_name = player["name"]
    return longest_name
print("Player with the longest name:", player_with_longest_name())