import Engine
import AI


# The frontend for the game
# All input from the user is done here
# Some logic is fone here to know what to ask for


def main():
    game = Engine.GameEngine(True,False)
    bot = AI.AI(3)

    # for i in range(0,18):
    #     (game.placeStone(i))

    while True:
        game.printBoard()

        if(game.is_game_done != ''):
            print("game is done")
            print(game.is_game_done)
            break

        if(game.player_one_turn):
            #TODO Create the flow of AI phases

            print("Player ones turn")
            if (game.player_one_phase == 1):
                print("Phase 1")
                if(game.player1_is_ai):
                    move = bot.getPlaceMove(game)
                    print("AI placed a stone on " + str(move) + " <---- ")
                    if (game.placeStone(move) == 'mill'):
                        move = bot.getRemoveStone(game)
                        print("AI Removed enemy stone at " + str(move))
                        game.removeStone(move)
                else:
                    place = input("Place stone on: ")
                    place = int(place)
                    if (game.placeStone(place) == 'mill'):
                        game.printBoard()
                        place = input("choose a enimy stone you want to remove:")
                        place = int(place)
                        game.removeStone(place)

            elif (game.player_one_phase == 2):
                print("Phase 2")
                print(game.player_one_turn)
                if(game.player1_is_ai):
                    initial_place, move = bot.getRotateMove(game)
                    print("AI moved stone from " + str(initial_place) + " -> " + str(move))
                    if (game.rotateStone(move, initial_place) == 'mill'):
                        move = bot.getRemoveStone(game)
                        print("AI Removed enemy stone at " + str(move))
                        game.removeStone(move)
                else:
                    initial_place = input("In which position is the stone you want to move? ")
                    initial_place = int(initial_place)
                    place = input("To which position do you want to move? ")
                    place = int(place)
                    if (game.rotateStone(place, initial_place) == 'mill'):
                        game.printBoard()
                        place = input("choose a enimy stone you want to remove:")
                        place = int(place)
                        game.removeStone(place)
            else:
                print("Phase 3")
                if(game.player1_is_ai):
                    initial_place, place = bot.getFlyingMove(game)
                    print("AI moved stone from " + str(initial_place) + " -> " + str(place))
                    if (game.flyingStone(place, initial_place) == 'mill'):
                        move = bot.getRemoveStone(game)
                        print("AI Removed enemy stone at " + str(move))
                        game.removeStone(move)
                else:
                    initial_place = input("In which position is the stone you want to move? ")
                    initial_place = int(initial_place)
                    place = input("To which position do you want to move? ")
                    place = int(place)
                    if (game.flyingStone(place, initial_place) == 'mill'):
                        game.printBoard()
                        place = input("choose a enimy stone you want to remove:")
                        place = int(place)
                        game.removeStone(place)


        else:
            print("Player two turn")
            if (game.player_two_phase == 1):
                print("Phase 1")
                place = input("place stone on: ")
                place = int(place)
                if (game.placeStone(place) == 'mill'):
                    game.printBoard()
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
                    game.printBoard()
                    place = input("choose a enimy stone you want to remove:")
                    place = int(place)
                    game.removeStone(place)

            else:
                print("Phase 3")
                initial_place = input("In which position is the stone you want to move? ")
                initial_place = int(initial_place)
                place = input("To which position do you want to move? ")
                place = int(place)
                if (game.flyingStone(place, initial_place) == 'mill'):
                    game.printBoard()
                    place = input("choose a enimy stone you want to remove:")
                    place = int(place)
                    game.removeStone(place)

main()
