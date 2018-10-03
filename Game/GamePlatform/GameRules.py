def detect_mill(board, move):
    current_stone = move.new
    mills = 0

    # Check if moving to this slot creates a mill with the next two stones in one direction
    if check_neighbours(current_stone, "top", move) == 3:
        mills += 1
    if check_neighbours(current_stone, "left", move) == 3:
        mills += 1
    if check_neighbours(current_stone, "right", move) == 3:
        mills += 1
    if check_neighbours(current_stone, "bottom", move) == 3:
        mills += 1

    # Check if moving to this slot creates a mill with the stones on each side (top,bottom and left,right) of this slot
    mills += check_each_side(current_stone, move)

    return mills


def check_neighbours(current_stone, direction, move):
    next_stone = None
    stone_count = 0

    if current_stone is not None and current_stone.owner is move.player:
        stone_count += 1

        next_stone = getattr(current_stone, direction)

        if next_stone is not None and next_stone.owner is move.player:
            stone_count += check_neighbours(next_stone, direction, move)

    return stone_count


def check_each_side(current_stone, move):
    one_side = None
    other_side = None

    mill_count = 0

    if current_stone is not None and current_stone.owner is move.player:
        # Check top and bottom
        if current_stone.top is not None and current_stone.bottom is not None:
            one_side = current_stone.top
            other_side = current_stone.bottom

            if one_side.owner is move.player and other_side.owner is move.player:
                mill_count += 1

        # Check left and right
        if current_stone.left is not None and current_stone.right is not None:
            one_side = current_stone.left
            other_side = current_stone.right

            if one_side.owner is move.player and other_side.owner is move.player:
                mill_count += 1

    return mill_count


def is_blocked(board, player):
    player_slots = board.get_all_player_slots(player)

    for current_position_slot in player_slots:
        neighbouring_slots = current_position_slot.get_neighbours()
        can_move = any(slot.owner is None for slot in neighbouring_slots)
        if can_move:
            return False

    return True


def who_has_less_than_three(board, players):
    # Checks if one of the players has less than three stones left. If yes, return that player

    for player in players:
        player_slots = board.get_all_player_slots(player)
        if len(player_slots) < 3:
            return player

    return None
