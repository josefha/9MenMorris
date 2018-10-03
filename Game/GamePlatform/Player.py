

class Player:
    def __init__(self, stone_type, tournament_player, n_stones):
        self.tournament_player = tournament_player
        self.stone_type = stone_type
        self.name = tournament_player.name
        self.n_stones = n_stones

    def set_controller(self, controller):
        self.controller = controller

    def __str__(self):
        return self.name + " (" + self.stone_type + ")"
