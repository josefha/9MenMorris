
import Engine
import random

class AI:
    complexity = 3 # 1 easy, # 2 medium , # 3 Complex

    def __init__(self, complexity):
        self.complexity = complexity

    def getStonesPos(self, game):
        char = game.getCurrentPlayerChar()
        positions = []
        for i, place in enumerate(game.board):
            if place == char:
                positions.append(i)
        return positions





    def getPlaceMove(self, game):
        char = game.getCurrentPlayerChar
        my_stones = self.getStonesPos(game)


        #place in middle positions if empty
        for place in [13,4,10,19]:
            if (game.board[place] == '_'):
                print("placed on a middle move")
                return place

        # not on easy ?
        # TODO FIX NOT WORKING
        # place a stone to get mill if possible
        for possible_mill in game.possible_mills:
            stones = 0
            empty = []
            for place in possible_mill:
                if(game.board[place] == char):
                    stones = stones + 1
                elif(game.board[place] == '_'):
                    empty.append(place)
            if(stones == 2 and len(empty) == 1):
                return empty[0]

        # TODO
        # place a stone to stop opponents mill <-

        # place a stone next to your own stone towords a mill
        # if last place in mill is empty
        for place in my_stones:
            for adj_place in game.adjecent_list[place]:
                for possible_mill in game.possible_mills:
                    if(place in possible_mill and adj_place in possible_mill):
                        print(possible_mill)
                        for pos in possible_mill:
                            if(game.board[pos] == '_'):
                                print("AI placed a second stone towards a mill")
                                return adj_place





        # TODO
        # place on next best positions after [13,4,10,16]

        empty_places = []
        for i, place in enumerate(game.board):
            if(place == '_'):
                empty_places.append(i)


        print("Made a random empty move, no good move was found")
        index = random.randrange(len(empty_places))
        print()
        return empty_places[index]




    # def getRotateMove(Game):
    #
    #     init_place = 0
    #     place = 1
    #
    #     return init_place, place
    #
    # def getFlytingMove(Game):
    #
    #     init_place = 0
    #     place = 1
    #
    #     return init_place, place
    #
    # def getRemoveMove(Game):
    #     place = 0
