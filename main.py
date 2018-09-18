class gameEngine:
    nr_turns = 0
    timer = 0
    player_one_turn = True
    player_two_turn = False
    stones_left_player_one = 9
    stones_left_player_two = 9
    board = ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',]
    

    def __init__(self):
        print("init")
                 #complexity = "difficult"

    #def startGame():
        #print("game has started")

    def makeMove(self, place):
        if ((place > 23 and place < 0) or self.board[place] != '_' ):
                 return ("not valid move")

        if (self.player_one_turn):
            if self.stones_left_player_one > 0:
                print ("player1")
                self.board[place] = "X"
                self.player_one_turn = False
                self.stones_left_player_one -= 1
                print(self.board)
            else:
                return ("no stones left")
        else:
            if self.stones_left_player_two > 0:
                print ("player2")
                self.board[place] = "O"
                self.player_one_turn = True
                self.stones_left_player_two -= 1
                print(self.board)
            else:
                return ("no stones left")

    
        


def main():
    game = gameEngine()
    #game.startGame()
    game.makeMove(22)
    game.makeMove(22)
    while True:
        place = input("Number?, if exit write x: ")
        if place == 'x': 
            break
        place = int(place)
        print (game.makeMove(place))
        

main()
    
    
