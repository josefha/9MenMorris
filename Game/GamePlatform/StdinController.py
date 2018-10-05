# -*- coding: utf-8 -*-
from GamePlatform.Controller import Controller
from GamePlatform.Move import Move


class StdinController(Controller):
    # during a players turn, display the currentPosition state of the board,
    # and ask for a move until a proper one is made
    def make_move(self, board, phase):
        # Get and validate input
        move = None
        if phase == 1:
            move = self.get_input_phase1(board)

        if phase == 2:
            move = self.get_input_phase2(board)

        if move is not None:
            self.perform_move(board, move)

        return move

    def get_input_slot(self, board, prompt):
        is_valid_input = False
        current_position_slot = None

        while not is_valid_input:

            # Where we are right now
            current_position = input(
                prompt +
                ":\033[93m Input is on the form <xy> (e.g. '41' for middle top) \u001b[0m"
            )

            has_two_letters = len(current_position) == 2
            if not has_two_letters:
                print(
                    "\033[31mPlease input two characters and two characters only.\u001b[0m"
                )
                continue
            first_is_valid = current_position[0].isdigit()
            second_is_valid = current_position[1].isdigit()
            current_position_slot = board.get_slot(current_position)
            is_valid_input = (has_two_letters and first_is_valid
                              and second_is_valid
                              and current_position_slot is not None)

            if current_position_slot is None:
                print(
                    "\033[31mThis slot does not exist. Select again.\u001b[0m")
            elif not is_valid_input:
                print("\033[31mPlease follow the format of <xy> "
                      "where x and y are each between 1-7: \u001b[0m")

        return current_position_slot

    def remove_stone(self, board):
        move = None
        is_valid_input = False
        while not is_valid_input:
            selected_slot = self.get_input_slot(
                board, "You got a mill! Select a stone to remove")
            slot_owner = selected_slot.owner

            slots_outside_mills = board.get_player_slots_outside_mills(
                slot_owner)

            if slot_owner is None or slot_owner is self.player:
                print("\033[31mYou have to select one of your opponents stones\u001b[0m")
            elif len(slots_outside_mills) > 0 and selected_slot not in slots_outside_mills:
                print("\033[31mYou have to remove stones not in a mill "
                      "before you remove stones inside a mill\u001b[0m")
            else:
                move = Move(self.player, None, selected_slot)
                is_valid_input = True

        self.perform_move(board, move)
        return move

    def get_input_phase1(self, board):
        move = None
        is_valid_input = False
        while not is_valid_input:
            selected_slot = self.get_input_slot(
                board, "Select a slot where you want to put your stone")
            if selected_slot.owner is not None:
                print("\033[31mSlot is already occupied, try again\u001b[0m")
            else:
                move = Move(self.player, selected_slot, None)
                is_valid_input = True
        return move

    def get_input_phase2(self, board):

        can_fly = len(board.get_all_player_slots(self.player)) == 3
        is_valid_input = False

        # Checks if the inputs are of the right formats
        while not is_valid_input:

            current_position_slot = self.get_input_slot(
                board, "Pick a stone to move")
            is_owner = current_position_slot.owner == self.player
            neighbouring_slots = current_position_slot.get_neighbours()
            can_move = any(slot.owner is None for slot in neighbouring_slots)

            if not is_owner:
                print("This stone is not yours. Select another.")
            elif not can_move and not can_fly:
                print("This stone can't move anywhere, pick another one")
            else:
                is_valid_input = True

        new_position_slot = None
        while new_position_slot is None:
            # Where we want to go
            if can_fly:
                chosen_slot = self.get_input_slot(
                    board, "Your stones can now fly: where do you want to go?")
                if chosen_slot.owner is None:
                    new_position_slot = chosen_slot
                    break
                else:
                    print("\033[31mSlot is already occupied, try again\u001b[0m")
                    continue

            new_position = input("Choose direction to move: ")

            while new_position not in ("up", "right", "left", "down"):
                new_position = input(
                    "You can only move up, right, left, or down")

            # Get a direction attribute, i.e. top/left/right/bottom
            direction = new_position
            if (direction == "up"):
                direction = "top"
            elif (direction == "down"):
                direction = "bottom"

            new_position_slot = getattr(current_position_slot, direction)

            if new_position_slot is None:
                print("There is no board slot in this direction. Try again!")
            elif new_position_slot.owner is not None:
                print("This slot is occupied by another stone. Try again!")
                new_position_slot = None

        return Move(self.player, new_position_slot, current_position_slot)
