
import Engine
import random

# TODO maybe need to remove game object from input for it work with every playform..

# AI Interface
# create AI bot with AI(complexity) --- 1 easy, 2 medium, 3 complex

#  Methods that can be used:
# .getPlaceMove(game)           --> Return a position (int)
# .getRotateMove(game)          --> Return two postions (int, int)
# .getFlyingMove(game)          --> Return two postions (int, int)
# .getRemoveStone(game)         --> Return a position (int)

class AI:
    # TODO choose whish rules that are going be for which complexity
    complexity = 3 # 1 easy, # 2 medium , # 3 complex

    def __init__(self, complexity):
        self.complexity = complexity

    def getEmptyPositions(self, game):
        empty_places = []
        for i, place in enumerate(game.board):
            if(place == '_'):
                empty_places.append(i)
        return empty_places

    # Returns positions of the current players stones
    def getStonesPos(self, game):
        char = game.getCurrentPlayerChar()
        positions = []
        for i, place in enumerate(game.board):
            if place == char:
                positions.append(i)
        return positions

    # PHASE 1 --- Returns a move to place a stone in first step
    def getPlaceMove(self, game):
        char = game.getCurrentPlayerChar()
        my_stones = self.getStonesPos(game)

        # Place in middle positions if empty
        for place in [13,4,10,19]:
            if (game.board[place] == '_'):
                print("placed on a middle move")
                return place

        # not on easy
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
                print(possible_mill)
                print(empty)
                return empty[0]

        # TODO
        # place a stone to stop opponents mill

        # place a stone next to your own stone towords a mill
        # if last place in mill is empty
        for place in my_stones:
            for adj_place in game.adjecent_list[place]:
                for possible_mill in game.possible_mills:
                    # TODO fix, check if your own stones... 
                    if(place in possible_mill and adj_place in possible_mill):
                        print(possible_mill)
                        for pos in possible_mill:
                            if(game.board[pos] == '_'):
                                print("AI placed a second stone towards a mill")
                                return adj_place





        # TODO
        # place on next best positions after [13,4,10,16]


        print("AI made a random move, no good move was found")
        empty_places = getEmptyPositions(game)
        index = random.randrange(len(empty_places))
        return empty_places[index]


    def getRemoveStone(self, Game):
        # NOTE that we have changed players turn before this turn

        # --> getCurrentPlayerChar() returns the opponents stones
        # insted of the players that actually are removing stones
        char = getCurrentPlayerChar(self, game)
        enemyStones = getStonesPos(self, game)

        # If enemy player can get a mill next turn remove one of those two stones
        for possible_mill in game.possible_mills:
            stones = 0
            empty = []
            enemy_places = []
            for place in possible_mill:
                if(game.board[place] == char):
                    stones = stones + 1
                    enemy_places.append(place)
                elif(game.board[place] == '_'):
                    empty.append(place)

            if(stones == 2 and len(empty) == 1):
                # Remove middle one or a random ?
                return enemy_places[1]

        # TODO
        # elif remove a stone that is two in a row

        # TODO
        # elif remove a middle stone ? []

        # else remove a random stone
        index = random.randrange(len(enemyStones))
        #return enemyStones[index]
        return

    # TODO
    # PHASE 2 --- Returns a move to rotate a stone in second step
    def getRotateMove(self, game):
        char = game.getCurrentPlayerChar()
        my_stones = self.getStonesPos(game)

        stone = 1
        move = 2

        return stone, move

    # TODO
    # PHASE 3 --- Returns a move to fly a stone in third step
    def getFlyingMove(self, game):
        char = game.getCurrentPlayerChar()
        my_stones = self.getStonesPos(game)

        stone = 1
        move = 2

        return stone, move
