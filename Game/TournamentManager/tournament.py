#!/usr/bin/python3
from operator import itemgetter, attrgetter
from random import shuffle
from GamePlatform.GameManager import GameManager
from GamePlatform.TerminalRenderer import TerminalRenderer
import random


class Player:
    def __init__(self, player_no, name, games_played, cpu, cpu_level, points):
        self.player_no = player_no
        self.name = name
        self.games_played = games_played
        self.cpu = cpu
        self.cpu_level = cpu_level
        self.points = points
        self.data = [player_no, name, games_played, cpu, cpu_level, points]

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __repr__(self):
        return repr((self.player_no, self.name, self.games_played, self.cpu, self.cpu_level, self.points))

    def display_player(self):
        print(str(self.player_no) + ".", "Name: ", self.name, ", Games played", self.games_played,
              ", CPU level: ", self.cpu_level, "Points: ", self.points)

    def update_player(self, point):
        self.points += point
        self.games_played += 1


def simulate_game(list_input):

    a = list_input[0][0]
    b = list_input[1][0]

    print("Next game will be between", players[a].name, "and", players[b].name+"!")

    if random.randint(0, 10) == 7:
        # gives player_no
        print("It's a draw between", players[a].name, "and", players[b].name+"!")
        players[a].update_player(1)
        players[b].update_player(1)
        winner = b
    else:
        shuffle(list_input)
        winner = list_input[0][0]
        loser = list_input[1][0]
        players[winner].update_player(3)
        players[loser].update_player(0)
        print(players[winner].name, "won!")
    return players[winner]


# Next Game Round Robin
def next_game_rr(num):
    # m_list = []
    all_games = []
    print_rr_table()
    total_games = int((num*((1+num)/2))-num)
    i = 1
    for x in range(0, num-1):
        for y in range(i, num):
            m_list = [players[x], players[y]]
            all_games.append(m_list)
        i += 1
    shuffle(all_games)
    sorted_list = sort_played(all_games)
    for x in range(0, total_games):
        print("Round", x+1)
        updated_list = update_list(sorted_list)
        sorted_list = sort_played(sorted_list)

        game_manager = GameManager(TerminalRenderer(), sorted_list[0])

        game_manager.start_game()

        # simulate_game(sorted_list[0])
        del sorted_list[0]
        print_rr_table()


# Generate Elimination Tournament
def elim_tourney(num):
    total_games = 0
    player_list = players
    table_list = []
    for x in range(0, num-1):
        table_list.append("Winner")
    print_t_table(table_list, num)
    while total_games < num-1:
        player_list, total_games = play_next_round(player_list, total_games, table_list, num)
    return player_list


def play_next_round(player_list, total_games, table_list, num):
    i = 0
    j = 0
    next_round = []
    while i < len(player_list):
        try:
            m_list = [players[player_list[i][0]], players[player_list[i+1][0]]]

            game_manager = GameManager(TerminalRenderer(), m_list)
            winner = game_manager.start_game()

            table_list[total_games] = winner.name
            print_t_table(table_list,num)
            total_games = total_games + 1
            next_round.append(players[winner[0]])
        except:
            next_round.append(players[player_list[i][0]])
        i = i+2
        j += 1
    return next_round, total_games


def print_t_table(m_list,list_input):
    max_width = name_width(players)
    if(list_input == 3):
        print("\n##########\n")
        print(players[0].name)
        print("-VS-".ljust(max_width),m_list[0])
        print(players[1].name)
        print("-VS-".rjust(max_width+6)+m_list[1].rjust(max_width+3)+"\n")
        print(players[2].name,players[2].name.rjust(max_width))
        print("\n##########\n")
    if(list_input == 4):
        print("\n##########\n")
        print(players[0].name)
        print("-VS-".ljust(max_width),m_list[0])
        print(players[1].name+"\n")
        print("-VS-".rjust(max_width+6)+m_list[2].rjust(max_width+3)+"\n")
        print(players[2].name)
        print("-VS-".ljust(max_width),m_list[1])
        print(players[3].name)
        print("\n##########\n")
    if(list_input == 5):
        print("\n##########\n")
        print(players[0].name)
        print("-VS-".ljust(max_width*2),m_list[0])
        print(players[1].name+"\n\n")
        print("-VS-".rjust((max_width*2)+6)+m_list[2].rjust(max_width+1))
        print(players[2].name)
        print("-VS-".ljust(max_width),m_list[1])
        print(players[3].name)
        print("-VS-".rjust(max_width+6)+m_list[3].rjust(max_width)+"\n")
        print(players[4].name,players[4].name.rjust(max_width))
        print("\n##########\n")
    if(list_input == 6):
        print("\n##########\n")
        print(players[0].name)
        print("-VS-".ljust(max_width),m_list[0])
        print(players[1].name+"\n")
        print("-VS-".rjust(max_width+6)+m_list[3].rjust(max_width+1)+"\n")
        print(players[2].name)
        print("-VS-".ljust(max_width),m_list[1])
        print(players[3].name)
        print("-VS-".rjust(max_width*2+6)+m_list[4].rjust(max_width+1)+"\n")
        print("\n\n"+players[4].name)
        print("-VS-".ljust(max_width*2),m_list[2])
        print(players[5].name)
        print("\n##########\n")
    if(list_input == 7):
        print("\n##########\n")
        print(players[0].name)
        print("-VS-".ljust(max_width),m_list[0])
        print(players[1].name+"\n")
        print("-VS-".rjust(max_width+6)+m_list[3].rjust(max_width+1)+"\n")
        print(players[2].name)
        print("-VS-".ljust(max_width),m_list[1])
        print(players[3].name)
        print("-VS-".rjust(max_width*2+6)+m_list[5].rjust(max_width+1)+"\n")
        print(players[4].name)
        print("-VS-".ljust(max_width),m_list[2])
        print(players[5].name)
        print("-VS-".rjust(max_width+6)+m_list[4].rjust(max_width+1)+"\n")
        print(players[6].name,players[6].name.rjust(max_width))
        print("\n##########\n")
    if(list_input == 8):
        print("\n##########\n")
        print(players[0].name)
        print("-VS-".ljust(max_width),m_list[0])
        print(players[1].name+"\n")
        print("-VS-".rjust(max_width+6)+m_list[4].rjust(max_width+1)+"\n")
        print(players[2].name)
        print("-VS-".ljust(max_width),m_list[1])
        print(players[3].name+"\n")
        print("-VS-".rjust(max_width*2+6)+m_list[6].rjust(max_width+1)+"\n")
        print(players[4].name)
        print("-VS-".ljust(max_width),m_list[2])
        print(players[5].name+"\n")
        print("-VS-".rjust(max_width+6)+m_list[5].rjust(max_width+1)+"\n")
        print(players[6].name)
        print("-VS-".ljust(max_width),m_list[3])
        print(players[7].name)
        print("\n##########\n")


def update_list(list_input):
    for x in range(0,len(list_input)):
        list_input[x][0][2] = players[list_input[x][0][0]].games_played
        list_input[x][1][2] = players[list_input[x][1][0]].games_played
    return list_input

def sort_played(list_input):
    sorted_list = sorted(list_input, key=lambda x: (x[0][2], x[1][2]))
    return sorted_list


def name_width(list_input):
    max_width = 4
    for elem in list_input:
        x = elem[0]
        width = len(players[x].name)
        if max_width < width:
            max_width = width
    return max_width


def print_rr_table():
    m_list = sorted(players, key=lambda player: player.points, reverse=True)
    i = 1
    max_width = name_width(m_list)
    print("  ", "Name".ljust(max_width), "| Played | Points")
    for elem in m_list:
        x = elem[0]
        print(str(i) + ".", players[x].name.ljust(max_width), "|  ",
              str(players[x].games_played), "   |  ", str(players[x].points))
        i += 1


def input_name(x, name_list):
    valid_name = False
    while valid_name == False:
        name = input("Input name for player " + str(x+1) + ":")
        valid_name = True
        if len(name) > 20:
            print("Please input a shorter name (less than 20 characters)")
            valid_name = False
        if len(name) < 1:
            valid_name = False
        if name in name_list:
            print("Someone already picked", name, "as their name")
            valid_name = False
        valid_name = not name.isspace()
    name_list.append(name)
    return name


def new_player_class(num, mode):
    name_list = []
    for x in range(0, num):
        player_no = x
        name = input_name(x, name_list)
        games_played = 0
        cpu = False
        cpu_level = 0
        points = 0

        if mode == 2 and x == 1:
            cpu = True
            cpu_level = select_cpu_level()

        if mode == 3:
            cpu = True
            cpu_level = select_cpu_level()

        if mode == 4 or mode == 5:
            cpu = select_cpu()
            if cpu == True:
                cpu_level = select_cpu_level()

        if cpu == True:
            name = name + "(CPU" + str(cpu_level) + ")"

        new_player = Player(player_no, name, games_played, cpu, cpu_level, points)
        players.append(new_player)

    return players


def select_cpu():
    selection = ""
    while selection != "y" and selection != "Y" and selection != "n" and selection != "N":
        selection = input("CPU controlled(y or n)?")
        if selection == "y" or selection == "Y":
            cpu = True

        if selection == "n" or selection == "N":
            cpu = False
    return cpu


def select_cpu_level():
    cpu_level = 0
    while cpu_level > 3 or cpu_level < 1:
        try:
            cpu_level = int(input("Input CPU difficulty (1-3):"))
        except ValueError:
            print("Please type in a number")
            continue

    return cpu_level


def select_game_type():
    selected_mode = 0
    while selected_mode > 6 or selected_mode < 1:
        try:
            selected_mode = int(input("Input mode:"))
            if selected_mode > 5 or selected_mode < 1:
                print("Input a number between 1 and 5")
        except ValueError:
            print("Please type in a number")
            continue
    return selected_mode


def input_players():
    no_of_players = 0
    while no_of_players > 8 or no_of_players < 3:
        try:
            no_of_players = int(input("How many players (between 3 and 8)? "))
            if no_of_players > 5 or no_of_players < 1:
                print("Input a number between 3 and 8")
        except ValueError:
            print("Please type in a number")
            continue
    return no_of_players


def start_menu():

    print("Welcome to <insert game name>!")
    print("Please input a game mode")
    print("1. Player vs Player")
    print("2. Player vs CPU")
    print("3. CPU vs CPU")
    print("4. Round robin tournament")
    print("5. Elimination tournament")

    mode = select_game_type()

    if mode == 1:
        print("Player vs player")
        new_player_class(2, mode)
        game_manager = GameManager(TerminalRenderer(), players)
        winner = game_manager.start_game()

    if mode == 2:
        print("Player vs CPU")
        new_player_class(2, mode)
        game_manager = GameManager(TerminalRenderer(), players)
        winner = game_manager.start_game()

    if mode == 3:
        print("CPU vs CPU")
        new_player_class(2, mode)
        game_manager = GameManager(TerminalRenderer(), players)
        winner = game_manager.start_game()

    if mode == 4:
        print("Round robin tournament selected")
        no_of_players = input_players()
        new_player_class(no_of_players, mode)
        next_game_rr(no_of_players)

    if mode == 5:
        print("Elimination tournament selected")
        no_of_players = input_players()
        new_player_class(no_of_players, mode)
        winner = elim_tourney(no_of_players)
        print(winner[0][1], "won the tournament!")
    if mode == 6:
        # Just a test mode
        new_player = Player(0, "Test1", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(1, "TestingALongName", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(2, "test3", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(3, "test4", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(4, "test5", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(5, "test6", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(6, "test7", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(7, "test8", 0, False, 0, 0)
        players.append(new_player)
        elim_tourney(8)


players = []
start_menu()
