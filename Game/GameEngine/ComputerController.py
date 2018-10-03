# -*- coding: utf-8 -*-
from GamePlatform.Controller import ../GamePlatform/Controller
from GamePlatform.Move import ../GamePlatform/Move

class ComputerController(Controller):
    # during a players turn, display the currentPosition state of the board,
    # and ask for a move until a proper one is made
    def make_move(self, board, phase):

        # TODO Get who turn it is

        # Get and validate input
        move = None
        if phase == 1:
            #move = self.get_input_phase1(board)

        if phase == 2:
            #move = self.get_input_phase2(board)

        if move is not None:
            #self.perform_move(board, move)

        return move


    def remove_stone(self, board):
        move = None

        self.perform_move(board, move)
        return move


        #TODO ADD AI Functions
