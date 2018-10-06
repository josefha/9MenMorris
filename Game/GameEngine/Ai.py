import random

#  Methods that can be used:
# .getPlaceMove(board, player_char)           --> Return a position (int)
# .getRotateMove(board, player_char)          --> Return two postions (int, int)
# .getFlyingMove(board, player_char)          --> Return two postions (int, int)
# .getRemoveStone(board, player_char)         --> Return a position (int)

class Ai:
    # TODO choose whish rules that are going be for which complexity
    complexity = 3 # 1 easy, # 2 medium , # 3 complex

    def __init__(self, complexity):
        self.complexity = complexity
        self.adjecent_list = [[1,9],[0,4,2],[1,14],[10,4],[1,3,7,5],
                     [4,13],[11,7],[4,6,8],[7,12],[0,21,10],
                     [3,9,11,18],[6,10,15],[8,13,17],[5,12,14,20],[2,13,23],
                     [11,16],[15,19,17],[12,16],[10,19],[16,18,20,22],
                     [13,19],[9,22],[19,21,23],[22,14]]


        self.possible_mills = [[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23],
                        [0,9,21],[3,10,18],[6,11,15],[1,4,7],[16,19,22],[8,12,17],[5,13,20],[2,14,23]]

    def getEmptyPositions(self, board):
        empty_places = []
        for i, place in enumerate(board):
            if(place == '_'):
                empty_places.append(i)
        return empty_places

    # Returns positions of the current players stones
    def getStonesPos(self, board, char):
        positions = []
        for i, place in enumerate(board):
            if place == char:
                positions.append(i)
        return positions

    def getStonesOpponentPos(self, board, char):
        if(char == 'X'):
            char = 'O'
        else:
            char = 'X'

        positions = []
        for i, place in enumerate(board):
            if place == char:
                positions.append(i)
        return positions

    def getOpponentPlayerChar(self, char):
        if(char == 'X'):
            return 'O'
        else:
            return 'X'


    # PHASE 1 --- Returns a move to place a stone in first step
    def getPlaceMove(self, board, player_char):
        char = player_char
        my_stones = self.getStonesPos(board, char)

        # place a stone to get mill if possible
        for possible_mill in self.possible_mills:
            stones = 0
            empty = []
            for place in possible_mill:
                if(board[place] == char):
                    stones = stones + 1
                elif(board[place] == '_'):
                    empty.append(place)

            if(stones == 2 and len(empty) == 1):
                return empty[0]

        # place a stone to stop opponents mill
        opponents_char = self.getOpponentPlayerChar(char)
        for possible_mill in self.possible_mills:
            stones = 0
            empty = []
            for place in possible_mill:
                if(board[place] == opponents_char):
                    stones = stones + 1
                elif(board[place] == '_'):
                    empty.append(place)

            if(stones == 2 and len(empty) == 1):
                return empty[0]

        # place a stone next to your own stone towords a mill
        # if last place in mill is empty
        for place in my_stones:
            print(place)
            for adj_place in self.adjecent_list[place]:
                if(board[adj_place] == '_'):
                    for possible_mill in self.possible_mills:
                        if(place in possible_mill and adj_place in possible_mill):
                            print(possible_mill)
                            empty_places_count = 0
                            for pos in possible_mill:
                                if(board[pos] == '_'):
                                    empty_places_count = empty_places_count + 1
                            if(empty_places_count == 2):
                                return adj_place

        # Place in middle positions if empty
        random_list = []
        for place in [13,4,10,19]:
            if (board[place] == '_'):
                random_list.append(place)


        if(len(random_list) > 0):
            random_number = random.choice(random_list)
            return (random_number)

        print("AI made a random move, no good move was found")
        empty_places = self.getEmptyPositions(board)
        index = random.randrange(len(empty_places))
        return empty_places[index]

    def getRemoveStone(self, board, player_char):
        # Change char to opponents char
        if(player_char == 'X'):
            char = 'O'
        else:
            char = 'X'

        enemyStones = self.getStonesPos(board, char)

        # If enemy player can get a mill next turn remove one of those two stones
        for possible_mill in self.possible_mills:
            stones = 0
            empty = []
            enemy_places = []
            for place in possible_mill:
                if(board[place] == char):
                    stones = stones + 1
                    enemy_places.append(place)
                elif(board[place] == '_'):
                    empty.append(place)

            if(stones == 2 and len(empty) == 1):
                return enemy_places[1]

        # Rule check, you should not be able to remove a stone
        # that already is in a mill if there are others
        for possible_mill in self.possible_mills:
            stones = 0
            empty = []
            enemy_places = []
            for place in possible_mill:
                if(board[place] == char):
                    stones = stones + 1
                    enemy_places.append(place)
                elif(board[place] == '_'):
                    empty.append(place)

            if(stones == 3 and len(empty) == 0):
                enemyStones.remove(enemy_places[0])
                enemyStones.remove(enemy_places[1])
                enemyStones.remove(enemy_places[2])


        if len(enemyStones) == 0:
            # remove an random stone if all are in mills
            enemyStones = self.getStonesPos(board, char)
            index = random.randrange(len(enemyStones))
            return enemyStones[index]
        else:
            # remove an random stone outside an mill
            index = random.randrange(len(enemyStones))
            return enemyStones[index]

    def simulateMove(self, board, stone_place, new_place):
        newBoard = board[:] # makes a copy of current board state
        char = newBoard[stone_place]
        newBoard[stone_place] = '_'
        newBoard[new_place] = char
        return newBoard

    # PHASE 2 --- Returns a move to rotate a stone in second step
    def getRotateMove(self, board, player_char):
        char = player_char
        my_stones = self.getStonesPos(board, char)
        empty_positions = self.getEmptyPositions(board)

        #Get possible moves
        possible_stones = []
        possible_postions = []
        for stone in my_stones:
            adj = []
            for place in self.adjecent_list[stone]:
                if (board[place] == '_'):
                    adj.append(place)
            if(len(adj) > 0):
                possible_stones.append(stone)
                possible_postions.append(adj)


        # Look for good moves to make
        # TODO
        for i,stone in enumerate(possible_stones):
            for position in possible_postions[i]:
                newBoard = self.simulateMove(board, stone, position)
                # check if move made a mill -> take it
                # remove moves that opens mills for the opponents
                # check if move blocked opponent mill (and did not open for a new mill)
                break

        print("made a random rotate move")
        print (possible_stones)
        print (possible_postions)

        p_i = random.randrange(len(possible_stones))
        s_i = random.randrange(len(possible_postions[p_i]))

        #e_i = random.randrange(len(empty_positions))
        init_place = possible_stones[p_i]
        move = possible_postions[p_i][s_i]

        return init_place, move

    # PHASE 3 --- Returns a move to fly a stone in third step
    def getFlyingMove(self, board, player_char):
        char = player_char
        my_stones = self.getStonesPos(board, player_char)
        empty_positions = self.getEmptyPositions(board)

        print("made a random flying move")
        s_i = random.randrange(len(my_stones))
        e_i = random.randrange(len(empty_positions))
        init_place = my_stones[s_i]
        move = empty_positions[e_i]

        return init_place, move
