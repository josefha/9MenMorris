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
    
    board = ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',]
    

    def __init__(self):
        print("init")
                 #complexity = "difficult"

    #def startGame():
        #print("game has started")

    def placeStone(self, place):
        if ((place > 23 and place < 0) or self.board[place] != '_' ):
                 return ("not valid move")

        if (self.player_one_turn):
            if self.stones_left_player_one > 0:
                print ("player1")
                self.board[place] = "X"
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
            self.player_one_turn = False
            print(self.board)

        else:
            print ("player2")
            self.board[place] = "O"
            self.board[initial_place] = "_"
            self.player_one_turn = True
            print(self.board)

    def flyingStone(self, place, initial_place):
        if ((place > 23 and place < 0) or self.board[place] != '_' ):
                 return ("not valid move")
                
        if (self.player_one_turn):
            print ("player1")
            self.board[place] = "X"
            self.board[initial_place] = "_"
            self.player_one_turn = False
            print(self.board)

        else:
            print ("player2")
            self.board[place] = "O"
            self.board[initial_place] = "_"
            self.player_one_turn = True
            print(self.board)
    
        

def main():
    game = gameEngine()
    #game.startGame()

    for i in range(0,16):
        (game.placeStone(i))

    while True:
        if(game.player_one_turn):
            if (game.player_one_phase == 1):
                print("Phase 1")
                place = input("Number? ")
                place = int(place)
                print (game.placeStone(place))
            elif (game.player_one_phase == 2):
                print("Phase 2")
                initial_place = input("In which position is the stone you want to move? ")
                initial_place = int(initial_place)
                place = input("To which position do you want to move? ")
                place = int(place)
                print (game.rotateStone(place, initial_place))
            else:
                print("Phase 3")
                initial_place = input("In which position is the stone you want to move? ")
                initial_place = int(initial_place)
                place = input("To which position do you want to move? ")
                place = int(place)
                print (game.rotateStone(place, initial_place))
            
                
        else:
            if (game.player_two_phase == 1):
                print("Phase 1")
                place = input("Number?, if exit write x: ")
                place = int(place)
                print (game.placeStone(place))
            elif (game.player_two_phase == 2):
                print("Phase 2")
                initial_place = input("In which position is the stone you want to move? ")
                initial_place = int(initial_place)
                place = input("To which position do you want to move? ")
                place = int(place)
                print (game.rotateStone(place, initial_place))
            else:
                print("Phase 3")
                initial_place = input("In which position is the stone you want to move? ")
                initial_place = int(initial_place)
                place = input("To which position do you want to move? ")
                place = int(place)
                print (game.rotateStone(place, initial_place))    
        

main()
    
    
