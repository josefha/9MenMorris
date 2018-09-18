class gameEngine:
    nr_turns = 0
    timer = 0
    player_one_turn = True
    player_two_turn = False
    stones_left_player_one = 9
    stones_left_player_two = 9
    player_one_phase = 1 #placing stone 1, rotating 2, flying 3
    player_two_phase = 1 #placing stone 1, rotating 2, flying 3
    adjecent_list = [[1,9],[0,4,2],[1,14],[10,4],[1,3,7,5],
                     [4,13],[11,7],[4,6,8],[7,12],[0,21,10],
                     [3,9,11,18],[6,10,15],[8,13,17],[5,12,14,20],[2,13,23],
                     [11,16],[15,19,17],[12,16],[10,19],[16,18,20,22],
                     [13,19],[9,22],[19,21,23],[22,14]]


    possible_mills = [[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23],
                        [0,9,21],[3,10,18],[6,11,15],[1,4,7],[16,19,22],[8,12,17],[5,13,20],[2,14,23]]

    board = ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',]


    def __init__(self):
        print("init")
                 #complexity = "difficult"

    def countStones():
        if (self.player_one_turn):
            char = 'X'
        else:
            char = 'O'

        counter = 0
        for i in self.board:
            if(i == char):
                counter += 1
        return counter

    def checkIfMill(self,place):
        if (self.player_one_turn):
            char = 'X'
        else:
            char = 'O'

        isMill = False
        for mill in self.possible_mills:
            if place in mill:
                counter = 0
                for stone in mill:
                    if(self.board[stone] == char):
                        counter += 1

                if counter == 3:
                    return(True)

        return False

    def removeStone(self,place):
        print("removing:" + str(place))

        if (self.player_one_turn):
            if(self.board[place] == 'X'):
                self.board[place] = '_'
                return True
        else:
            if(self.board[place] == 'O'):
                self.board[place] = '_'
                return True

        return False





    def placeStone(self, place):
        if ((place > 23 and place < 0) or self.board[place] != '_' ):
                 return ("not valid move")

        if (self.player_one_turn):
            if self.stones_left_player_one > 0:
                print ("player1")
                self.board[place] = "X"

                if(self.checkIfMill(place)):
                    return('mill')

                self.player_one_turn = False
                self.stones_left_player_one -= 1
                print(self.board)
                if self.stones_left_player_one == 0:
                    self.player_one_phase = 2
            else:
                return ("no stones left")
        else:
            if self.stones_left_player_two > 0:
                print ("player2")
                self.board[place] = "O"

                if(self.checkIfMill(place)):
                    return('mill')

                self.player_one_turn = True
                self.stones_left_player_two -= 1
                print(self.board)


                if self.stones_left_player_two == 0:
                    self.player_two_phase = 2
            else:
                return ("no stones left")



    def rotateStone(self, place, initial_place):
        if ((place > 23 and place < 0) or self.board[place] != '_' ):
                 return ("not valid move")
        if place not in self.adjecent_list[initial_place]:
            return ("Not a adjecent node")

        if (self.player_one_turn):
            print ("player1")
            self.board[place] = "X"
            self.board[initial_place] = "_"
            if(self.checkIfMill(place)):
                return('mill')

            self.player_one_turn = False
            print(self.board)

        else:
            print ("player2")
            self.board[place] = "O"
            self.board[initial_place] = "_"
            if(self.checkIfMill(place)):
                return('mill')

            self.player_one_turn = True
            print(self.board)

        if(self.checkIfMill(place)):
            return('mill')
        else:
            return('')

    def flyingStone(self, place, initial_place):
        if ((place > 23 and place < 0) or self.board[place] != '_' ):
                 return ("not valid move")

        if (self.player_one_turn):
            print ("player1")
            self.board[place] = "X"
            self.board[initial_place] = "_"
            if(self.checkIfMill(place)):
                return('mill')
            self.player_one_turn = False
            print(self.board)

        else:
            print ("player2")
            self.board[place] = "O"
            self.board[initial_place] = "_"
            if(self.checkIfMill(place)):
                return('mill')
            self.player_one_turn = True
            print(self.board)


def main():
    game = gameEngine()
    #game.startGame()

    # for i in range(0,18):
    #     (game.placeStone(i))

    while True:
        if(game.player_one_turn):
            if (game.player_one_phase == 1):
                print("Phase 1")
                place = input("Number? ")
                place = int(place)
                if (game.placeStone(place) == 'mill'):
                    place = input("choose a enimy stone you want to remove:")
                    place = int(place)
                    game.removeStone(place)

            elif (game.player_one_phase == 2):
                print("Phase 2")
                initial_place = input("In which position is the stone you want to move? ")
                initial_place = int(initial_place)
                place = input("To which position do you want to move? ")
                place = int(place)
                if (game.rotateStone(place, initial_place) == 'mill'):
                    place = input("choose a enimy stone you want to remove:")
                    place = int(place)
                    game.removeStone(place)
            else:
                print("Phase 3")
                initial_place = input("In which position is the stone you want to move? ")
                initial_place = int(initial_place)
                place = input("To which position do you want to move? ")
                place = int(place)
                print ()
                if (game.flyingStone(place, initial_place == 'mill')):
                    place = input("choose a enimy stone you want to remove:")
                    place = int(place)
                    game.removeStone(place)


        else:
            if (game.player_two_phase == 1):
                print("Phase 1")
                place = input("Number?, if exit write x: ")
                place = int(place)
                if (game.placeStone(place) == 'mill'):
                    place = input("choose a enimy stone you want to remove:")
                    place = int(place)
                    game.removeStone(place)

            elif (game.player_two_phase == 2):
                print("Phase 2")
                initial_place = input("In which position is the stone you want to move? ")
                initial_place = int(initial_place)
                place = input("To which position do you want to move? ")
                place = int(place)

                if (game.rotateStone(place, initial_place) == 'mill'):
                    place = input("choose a enimy stone you want to remove:")
                    place = int(place)
                    game.removeStone(place)

            else:
                print("Phase 3")
                initial_place = input("In which position is the stone you want to move? ")
                initial_place = int(initial_place)
                place = input("To which position do you want to move? ")
                place = int(place)
                if (game.flyingStone(place, initial_place == 'mill')):
                    place = input("choose a enimy stone you want to remove:")
                    place = int(place)
                    game.removeStone(place)


main()
