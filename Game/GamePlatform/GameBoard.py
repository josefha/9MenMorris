# -*- coding: utf-8 -*-
from __future__ import print_function
from GamePlatform.BoardSlot import BoardSlot

board_layout = """
x--x--x
|x-x-x|
||xxx||
xxx xxx
||xxx||
|x-x-x|
x--x--x"""


class GameBoard:
    def __init__(self):
        self.positions = []
        self.board = {}
        board_rows = board_layout.strip().split("\n")
        row_count = 1
        for row in board_rows:
            columnt_count = 1
            for char in row:
                position = str(columnt_count) + str(row_count)
                if char == 'x':
                    self.positions.append(position)
                    self.board[position] = BoardSlot(position, None)
                    char_to_left = row[columnt_count-1-1]
                    char_to_top = board_rows[row_count - 1 - 1][columnt_count - 1]

                    if (char_to_left == 'x' or char_to_left == '-') and columnt_count > 1:
                        slot_to_left = self.get_left(position)
                        slot_to_left.set_right(self.board[position])
                        self.board[position].set_left(slot_to_left)

                    if (char_to_top == 'x' or char_to_top == '|') and row_count > 1:
                        slot_to_top = self.get_top(position)
                        slot_to_top.set_bottom(self.board[position])
                        self.board[position].set_top(slot_to_top)

                columnt_count += 1
            row_count += 1



    def get_left(self, position):
        column = position[0]
        row = position[1]
        for x in reversed(range(1, int(column))):
            if (str(x) + row) in self.board:
                return self.board[str(x) + row]
        return None

    def get_right(self, position):
        column = position[0]
        row = position[1]
        for x in range(int(column) + 1, 8):
            if (str(x) + row) in self.board:
                return self.board[str(x) + row]
        return None

    def get_top(self, position):
        column = position[0]
        row = position[1]
        for y in reversed(range(1, int(row))):
            if (column + str(y)) in self.board:
                return self.board[column + str(y)]
        return None

    def get_bottom(self, position):
        column = position[0]
        row = position[1]
        for y in range(int(row) + 1, 8):
            if (column + str(y)) in self.board:
                return self.board[column + str(y)]
        return None

    def get_slot(self, position):
        if position in self.board:
            return self.board[position]
        return None

    def set_slot(self, position, owner):
        slot = self.get_slot(position)
        if slot is not None:
            slot.owner = owner

    def unset_slot(self, position):
        slot = self.get_slot(position)
        if slot is not None:
            slot.owner = None

    def get_all_player_slots(self, player):
        player_slots = []
        for slot in self.board.values():
            if slot.owner == player:
                player_slots.append(slot)
        return player_slots
