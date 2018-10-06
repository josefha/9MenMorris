from abc import ABC, abstractmethod


class Controller(ABC):
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def make_move(self, board, phase):
        pass

    def perform_move(self, board, move):
        # Then we have placed a stone

        if move.new is not None and move.old is None:
            move.new.owner = self.player

        # Then we have moved a stone
        if move.new is not None and move.old is not None:
            move.old.owner = None
            move.new.owner = self.player

        # Then we have removed a stone
        if move.new is None and move.old is not None:
            move.old.owner = None
