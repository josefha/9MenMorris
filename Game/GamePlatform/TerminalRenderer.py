import os

UU_GAME_TEXT = r"""
  _    _ _    _         _____
 | |  | | |  | |       / ____|
 | |  | | |  | |______| |  __  __ _ _ __ ___   ___
 | |  | | |  | |______| | |_ |/ _` | '_ ` _ \ / _ \
 | |__| | |__| |      | |__| | (_| | | | | | |  __/
  \____/ \____/        \_____|\__,_|_| |_| |_|\___|

                                                   """

class TerminalRenderer:
    def begin_render(self):
        # cls clears the screen on windows (nt), unix uses clear command
        os.system('cls' if os.name == 'nt' else 'clear')
        print(UU_GAME_TEXT)

    def print_player_turn(self, player):
        print("It is", player, "'s turn")

    def print_player_stones(self, players):
        for player in players:
            print(player, "have", player.n_stones, "left")

    def render_phase(self, phase):
        if phase == 1:
            print("Current Phase:", phase, "'Placing Stones'")
        elif phase == 2:
            print("Current Phase:", phase, "'Moving Stones'")

    def render_winner(self, winner):
        # cls clears the screen on windows (nt), unix uses clear command
        os.system('cls' if os.name == 'nt' else 'clear')
        if winner is None:
            print("No one won")
        else:
            print("\033[92mWinner is", winner, "Congratulations!\u001b[0m")

    def render(self, board):
        board_str = ""
        for row in range(1, 8):
            board_str += str(row) + " | "
            for column in range(1, 8):
                position = str(column) + str(row)

                slot_to_left = board.get_left(position)
                slot_to_right = board.get_right(position)

                has_left = (slot_to_left is not None and
                            slot_to_left.right is not None)
                has_right = (slot_to_right is not None and
                             slot_to_right.left is not None)

                slot_to_bottom = board.get_bottom(position)
                has_bottom = (slot_to_bottom is not None and
                              slot_to_bottom.top is not None)

                slot = board.get_slot(position)
                if slot is not None:
                    board_str += "—" if has_left else " "
                    if slot.owner is None:
                        board_str += "□"
                    else:
                        if slot.owner.stone_type == "black":
                            board_str += "B"
                        else:
                            board_str += "W"
                    board_str += "—" if has_right else " "
                elif has_left and has_right:
                    board_str += "———"
                elif has_bottom:
                    board_str += " | "
                else:
                    board_str += "   "
            board_str += "\n  | "
            for column in range(1, 8):
                position = str(column) + str(row)
                slot_to_bottom = board.get_bottom(position)
                has_bottom = (slot_to_bottom is not None and
                              slot_to_bottom.top is not None)
                if has_bottom:
                    board_str += " | "
                else:
                    board_str += "   "
            board_str += "\n"
        board_str += " " * 4
        for column in range(1, 8):
            board_str += "———"
        board_str += "\n" + " " * 4
        for column in range(1, 8):
            board_str += " " + str(column) + " "

        print(board_str)
