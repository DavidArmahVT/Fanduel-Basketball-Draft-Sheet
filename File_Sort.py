import FileReader as reader

todays_file = "Fanduel_example.csv"  # update file for each day


# Deletes all injured players from the list provided
# players_list list of players
def delete_injured_players(players_list):
    # Loops through list provided
    for i in players_list:
        # Checks if a player is Out
        if i[6] == '0':
            players_list.remove(i)  # Removes player from the list
    return players_list  # returns list with healthy players

# Sorts list by players name
# players_list list of players
def sortPlayer_names(players_list):
    players_list.sort(key=lambda x: x[0])  # sorts based on first name, first element in tuple
    return players_list  # sorted names player list


# Sorts list by players position
# players_list list of players
def sortPlayer_positions(players_list):
    players_list.sort(key=lambda x: x[1])  # sorts based on positon
    return players_list  # sorts names player list


# Sorts list by teams
def sortPlayer_teams(players_list):
    players_list.sort(key=lambda x: x[2])  # sorts based on team
    return players_list  # returns sorted list


# Sorts list by opposing opponents
def sortPlayer_opponents(players_list):
    players_list.sort(key=lambda x: x[3])  # sorts by players opposing team
    return players_list  # returns sorted list of players opposing teams


# Sorts list by players prices
def sortPlayer_price(players_list):
    players_list.sort(key=lambda x: x[4])  # sorts by a players price
    return players_list  # returns new sorted list


# sorts list by players fanduel pt average
def sortPlayer_FDAVG(players_list):
    players_list.sort(key=lambda x: x[5])  # sorts by players fanduel point average
    return players_list
#INCOMPLETE
def sortPlayer_Value(players_list):
    return players_list
#INCOMPLETE
def sortPlayer_Potential(players_list):
    return players_list


# sorts list of players by specific team
def sort_team(players_list, team):
    team_list = []  # empty list to sort players of the same team

    for i in players_list:  # loops through the list provided

        if i[2] == team:  # looks if element in 2nd position in tuple is the same as the team we are looking for
            team_list.append(i)  # adds the player to the team_list if they are on the team we are looking for
    return team_list  # returns the list of players from the team


# sorts list of players by specific position
def sort_position(players_list, position):
    position_list = []  # empty list
    for i in players_list:  # loops through the list provided
        if i[1] == position:  # checks element in first position in tuple is the same as the position we are looking for
            position_list.append(i)  # adds player to position_list if they are of the position we are looking for
    return position_list  # returns list of positions we want to have


# gets price of player we are looking for
# player_name name of the player
def get_Price(players_list, player_name):
    for i in players_list:  # loops through the list provided
        if i[0] == player_name:  # if their name is the same as the name we are looking for
            return i[4]  # return the price of the player
    else:  # if player is not in list
        return player_name + " " + 'is not playing today'


# gets positon of player we are looking for
def get_Position(players_list, player_name):
    for i in players_list:  # loops through the list provided
        if i[0] == player_name:  # if name in list is equal to the name we are looking for
            return i[1]  # return the players position
    else:  # if player is not in list
        return player_name + " " + 'is not playing today'


# gets the team of the player we are  looking for
def get_Team(players_list, player_name):
    for i in players_list:  # loops through the player_list
        if i[0] == player_name:  # if the name is equal to the name we want to look for
            return i[2]  # return the players team
    else:  # if player is not in list
        return player_name + " " + 'is not playing today'


# gets the opponenet of the player we are looking for
def get_Opponent(players_list, player_name):
    for i in players_list:  # loops through the list
        if i[0] == player_name:  # if the name is the same as the one we are looking for
            return i[3]  # return the players opponent they are facing today
    else:  # if player is not in list
        return player_name + " " + 'is not playing today'


# gets the players fanduel ppg average
def get_fdp_AVG(players_list, player_name):
    for i in players_list:  # loops through the list
        if i[0] == player_name:  # if the player is in our list
            return i[5]  # return the players fanduel ppg average
    else:  # if player is not in list
        return player_name + " " + 'is not playing today'


# checks the health of a player we are looking for
def get_Health(players_list, player_name):
    for i in players_list:  # loops through the list
        if i[0] == player_name:  # if the player we are looking for is in the list
            if i[6] == 'O':  # checks if the player is out
                return player_name + " " + 'is Out'
            elif i[6] == 'GTD':  # checks if they are unsure
                return player_name + " " + 'is a Game-Time Decision.'
            else:
                # then the player must be healthy
                return player_name + " " + 'is Healthy'
    else:  # if player is not in list
        return player_name + " " + 'is not playing today'

# print(injured_players(read_files(todays_file)))   # list of injured players
# print(read_files(todays_file)) # list of todays full players list
# print(sortbyPlayer_price(injured_players(read_files(todays_file)))) # list of healthy players sorted by price
# print(playersByTeam(read_files(todays_file), 'DET'))
# print(sort_position(read_files(todays_file), 'PG'))
# print(get_Health(read_files(todays_file), 'Awad'))
# print(sort_team(reader.read_files(todays_file), 'DET'))
