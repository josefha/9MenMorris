import random
from time import sleep

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

    # Returns empty postions in board
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

    # Returns postions of opponents stones
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
    # Returns opponents player character
    def getOpponentPlayerChar(self, char):
        if(char == 'X'):
            return 'O'
        else:
            return 'X'

    # Returns a board with a move made
    def simulateMove(self, board, stone_place, new_place):
        newBoard = board[:] # makes a copy of current board state
        char = newBoard[stone_place]
        newBoard[stone_place] = '_'
        newBoard[new_place] = char
        return newBoard

    # PHASE 1 --- Returns a move to place a stone in first step
    def getPlaceMove(self, board, player_char):
        char = player_char
        my_stones = self.getStonesPos(board, char)

        if (self.complexity != 1):
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

            if (self.complexity == 3):
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
                for adj_place in self.adjecent_list[place]:
                    if(board[adj_place] == '_'):
                        for possible_mill in self.possible_mills:
                            if(place in possible_mill and adj_place in possible_mill):
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

        empty_places = self.getEmptyPositions(board)
        index = random.randrange(len(empty_places))
        return empty_places[index]

    # Returns a move to remove an opponent stone
    def getRemoveStone(self, board, player_char):
        # Change char to opponents char
        if(player_char == 'X'):
            char = 'O'
        else:
            char = 'X'

        enemyStones = self.getStonesPos(board, char)

        if (self.complexity != 1):
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
                for i in range(3):
                    if enemy_places[i] in enemyStones:
                        enemyStones.remove(enemy_places[i])


        if len(enemyStones) == 0:
            # remove an random stone if all are in mills
            enemyStones = self.getStonesPos(board, char)
            index = random.randrange(len(enemyStones))
            return enemyStones[index]
        else:
            # remove an random stone outside an mill
            index = random.randrange(len(enemyStones))
            return enemyStones[index]

    # PHASE 2 --- Returns a move to rotate a stone in second step
    def getRotateMove(self, board, player_char):
        char = player_char
        my_stones = self.getStonesPos(board, char)
        opponents_char = self.getOpponentPlayerChar(char)

        # Get all possible moves
        possible_stones = []
        possible_positions = []
        for stone in my_stones:
            adj = []
            for place in self.adjecent_list[stone]:
                if (board[place] == '_'):
                    adj.append(place)
            if(len(adj) > 0):
                possible_stones.append(stone)
                possible_positions.append(adj)


        better_possible_stones = possible_stones[:]
        better_possible_positions = possible_positions[:]

        if (self.complexity == 1):
            # make a random move if no good move is availible
            result_possible_stones = possible_stones[:]
            result_possible_positions = possible_positions[:]

            for index, stone in enumerate(possible_stones):
                if possible_positions[index] == []:
                    del result_possible_stones[index]
                    del result_possible_positions[index]
            p_i = random.randrange(len(result_possible_stones))
            s_i = random.randrange(len(result_possible_positions[p_i]))
            init_place = result_possible_stones[p_i]
            move = result_possible_positions[p_i][s_i]
            return init_place, move
        # Look for if mill is possible and remove really bad moves
        for index,stone in enumerate(possible_stones):
            for position in possible_positions[index]:
                newBoard = self.simulateMove(board, stone, position)
                # check if move made a mill -> take it
                for mill in self.possible_mills:
                    if position in mill:
                        count = 0
                        for place in mill:
                            if(newBoard[place] == char):
                                count = count + 1
                        if(count == 3):
                            return stone, position
                if (self.complexity == 3):
                    # remove moves that opens mills for the opponents
                    for mill in self.possible_mills:
                        if stone in mill:
                            count = 0
                            enemy_stones_in_mill = []
                            for place in mill:
                                if(newBoard[place] == opponents_char):
                                    count = count + 1
                                    enemy_stones_in_mill.append(place)

                            # if we oppened a mill -> check if any enemy stone can move there
                            if(count == 2):
                                all_enemy_stones = self.getStonesOpponentPos(newBoard, char)
                                for enemy_stone in enemy_stones_in_mill:
                                    all_enemy_stones.remove(enemy_stone)

                                for enemy_stone in all_enemy_stones:
                                    if stone in self.adjecent_list[enemy_stone]:
                                        # Now we now that our move made it possible for
                                        # and oppononent mill -> remove it from new
                                        # index = index of the current stone we want to move
                                        better_possible_positions[index].remove(position)


        # Check if a move blocks an opponent mill -> take it
        # If the move oppened for another opponent mill
        # it has already been removed
        for index,stone in enumerate(possible_stones):
            for position in possible_positions[index]:
                newBoard = self.simulateMove(board, stone, position)
                for mill in self.possible_mills:
                    if position in mill:
                        count = 0
                        enemy_stones_in_mill = []
                        for place in mill:
                            if(newBoard[place] == opponents_char):
                                count = count + 1
                                enemy_stones_in_mill.append(place)
                        if(count == 2):
                            # Now we have moved to a place where where opponent
                            # had two stones in a row -> check if any other
                            # of opponents stones could move there -> if so block it
                            all_enemy_stones = self.getStonesOpponentPos(newBoard, char)
                            for enemy_stone in enemy_stones_in_mill:
                                all_enemy_stones.remove(enemy_stone)

                            for enemy_stone in all_enemy_stones:
                                if position in self.adjecent_list[enemy_stone]:
                                    #Make a blocking move
                                    return stone, position


        # Really bad moves are removed and there is no mill possible
        # and we also can't block opponent mills
        # -> check if there are good two turns move to get a mill

        possible_two_step_moves = [] # save moves that are possible two step to a mill

        for index,stone in enumerate(better_possible_stones):
            for position in better_possible_positions[index]:
                newBoard = self.simulateMove(board, stone, position)
                # Check if two steps simulate can form a mill
                # for stone in new position, can it form a mill?
                # take it if opponent can't block it next turn

                # Simulate one more move for every simulated move
                s_my_stones = self.getStonesPos(newBoard, char)
                s_possible_stones = []
                s_possible_positions = []
                for my_stone in s_my_stones:
                    adj = []
                    for place in self.adjecent_list[my_stone]:
                        if (newBoard[place] == '_'):
                            adj.append(place)
                    if(len(adj) > 0):
                        s_possible_stones.append(my_stone)
                        s_possible_positions.append(adj)

                for s_index, s_stone in enumerate(s_possible_stones):
                    for s_position in s_possible_positions[s_index]:
                        s_newBoard = self.simulateMove(newBoard, s_stone, s_position)
                        # s_newBoard we have simulated two moves from board
                        # (and we skipped opponents move)


                        for mill in self.possible_mills:
                            if s_position in mill:
                                count = 0
                                for place in mill:
                                    if(s_newBoard[place] == char):
                                        count = count + 1

                                if(count == 3):
                                    # here we found two moves who led to a mill
                                    # now check if opponent can block it

                                    # This is after one simulated move
                                    all_enemy_stones = self.getStonesOpponentPos(newBoard, char)

                                    good_move = True
                                    for enemy_stone in all_enemy_stones:
                                        if s_position in self.adjecent_list[enemy_stone]:
                                            # Here the opponent could block the mill
                                            # before we get a chance make two moves
                                            good_move = False
                                            break

                                    # enemy could not block two step move -> add it
                                    if(good_move):
                                        possible_two_step_moves.append([stone, position])

        # make one of the moves towards a mill if oppponent cant block it
        if (len(possible_two_step_moves) > 0):
            sleep(1)
            index = random.randrange(len(possible_two_step_moves))
            init_place = possible_two_step_moves[index][0]
            move = possible_two_step_moves[index][1]
            return init_place, move


        result_possible_stones = better_possible_stones[:]
        result_possible_positions = better_possible_positions[:]

        # Remove stone from possible moves if there are not any moves it can make
        i = 0
        for index, stone in enumerate(better_possible_stones):
            if (len(better_possible_positions[index]) == 0):
                del result_possible_stones[i]
                del result_possible_positions[i]
            else:
                i = i + 1

        if(len(result_possible_stones) == 0):
            # make a random move if no good move is availible
            result_possible_stones = possible_stones[:]
            result_possible_positions = possible_positions[:]

            # Removes stone that can't move any direction..
            i = 0
            for index, stone in enumerate(possible_stones):
                if len(possible_positions[index]) == 1:
                    del result_possible_stones[i]
                    del result_possible_positions[i]
                else:
                    i = i + 1
            p_i = random.randrange(len(result_possible_stones))
            s_i = random.randrange(len(result_possible_positions[p_i]))
            init_place = result_possible_stones[p_i]
            move = result_possible_positions[p_i][s_i]
            return init_place, move
        else:
            # make a random move of the ones that are not bad
            p_i = random.randrange(len(result_possible_stones))
            s_i = random.randrange(len(result_possible_positions[p_i]))
            init_place = result_possible_stones[p_i]
            move = result_possible_positions[p_i][s_i]

            return init_place, move

    # PHASE 3 --- Returns a move to fly a stone in third step
    def getFlyingMove(self, board, player_char):
        char = player_char
        my_stones = self.getStonesPos(board, player_char)
        empty_positions = self.getEmptyPositions(board)

        if(self.complexity != 1):
            # Move to mill if possible
            for mill in self.possible_mills:
                count = 0
                empty_pos = []
                for position in mill:
                    if(board[position] == char):
                        count = count + 1
                    elif(board[position] == '_'):
                        empty_pos.append(position)

                # if we can move to a mill
                if(count == 2 and len(empty_pos) == 1):
                    my_stones = self.getStonesPos(board, char)
                    for stone in my_stones:
                        if(stone not in mill):
                            return stone, empty_pos[0]

            # fly stone towards a mill if rest of mill is empty
            for place in my_stones:
                for adj_place in self.adjecent_list[place]:
                    if(board[adj_place] == '_'):
                        for possible_mill in self.possible_mills:
                            if(place in possible_mill and adj_place in possible_mill):
                                empty_places_count = 0
                                for pos in possible_mill:
                                    if(board[pos] == '_'):
                                        empty_places_count = empty_places_count + 1
                                if(empty_places_count == 2):
                                    # get which stone to move
                                    init_place = my_stones[0]
                                    for my_stone in my_stones:
                                        if (my_stone != place):
                                            init_place = my_stone
                                            break
                                    return my_stone, adj_place

        s_i = random.randrange(len(my_stones))
        e_i = random.randrange(len(empty_positions))
        init_place = my_stones[s_i]
        move = empty_positions[e_i]

        return init_place, move
