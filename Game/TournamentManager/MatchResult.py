class MatchResult:
    def __init__(self, player):
        self.player = player
        self.data = [player]

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __repr__(self):
        return repr((self.player))
