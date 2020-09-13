import os
def read_file(filename):
    filename = open(filename)
    categories = filename.readline()  # doesnt count top line

    player_list = {}  # creates dictionary

    for line in filename:
        line = line.rstrip('\n')  # strip off the end-of-line marker, '\n'
        line = line.split(',')  # split the players into a string list by a comma
        player_name = line[3].strip() # players nick name
        position = line[1].strip() # players position
        fdp_avg = round(float(line[5]), 2) #players fdp avg with a 2 decimal round system
        price = line[7].strip() #price of player
        team = line[9].strip() #team player is on
        opponent = line[10].strip() # opponent
        injury = line[11].strip() # does player have a injury?

        value = ( position, team, opponent,  price, fdp_avg, injury)  # adds player to tuple

        player_list[player_name] = value  # adds to dictionary
    return player_list