# -*- coding: utf-8 -*-
from GamePlatform.Controller import Controller
from GamePlatform.Move import Move
from GameEngine.BoardTranslator import BoardTranslator
from GameEngine.Ai import Ai


class ComputerController(Controller):
    # during a players turn, display the currentPosition state of the board,
    # and ask for a move until a proper one is made

    def __init__(self, player, complexity):
        self.player = player
        self.bot = Ai(complexity)
        self.translator = BoardTranslator()

    def make_move(self, board, phase):
        old_board = self.translator.getOldBoard(board.board)
        player_char = self.translator.getCurrentPlayerChar(self.player)

        if phase == 1:
            ai_move = self.bot.getPlaceMove(old_board, player_char)
            selected_postion = self.translator.getNewPos(ai_move)
            move = Move(self.player, board.get_slot(selected_postion), None)

        if phase == 2:
            can_fly = len(board.get_all_player_slots(self.player)) == 3
            if(can_fly):
                init_place, next_place = self.bot.getFlyingMove(old_board, player_char)
            else:
                init_place, next_place = self.bot.getRotateMove(old_board, player_char)

            selected_init_postion = self.translator.getNewPos(init_place)
            selected_next_postion = self.translator.getNewPos(next_place)
            move = Move(self.player, board.get_slot(selected_next_postion), board.get_slot(selected_init_postion))

        if move is not None:
            self.perform_move(board, move)

        return move


    def remove_stone(self, board):
        move = None

        old_board = self.translator.getOldBoard(board.board)
        player_char = self.translator.getCurrentPlayerChar(self.player)
        ai_move = self.bot.getRemoveStone(old_board, player_char)
        selected_postion = self.translator.getNewPos(ai_move)

        move = Move(self.player, None, board.get_slot(selected_postion))
        self.perform_move(board, move)
        return move
