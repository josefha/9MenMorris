
import Engine

class AI:
    complexity = 3 # 1 easy, # 2 medium , # 3 Complex


    def __init__(self, complexity):
        self.complexity = complexity

    def getStonesPos(game):

        char = game.getCurrentPlayerChar
        positions = []
        for i, place in enumerate(game.board):
            if place == char:
                positions.append(i)

        return positions





    def getPlaceMove(self, game):
        place = 0
        char = game.getCurrentPlayerChar

        for place in [13,4,10,16]:
            if (game.board[place] == '_'):
                return place
        for place in self.getStonesPos(game):
            for best_place in game.adjecent_list[place]:
                if game.board[best_place] == char:







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
    #     return place
