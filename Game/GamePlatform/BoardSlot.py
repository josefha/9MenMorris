class BoardSlot:
    def __init__(self, position, owner):
        self.position = position
        self.owner = owner
        self.right = None
        self.top = None
        self.bottom = None
        self.left = None

    def set_right(self, right):
        self.right = right

    def set_top(self, top):
        self.top = top

    def set_bottom(self, bottom):
        self.bottom = bottom

    def set_left(self, left):
        self.left = left

    def get_neighbours(self):
        return [
            slot for slot in [self.top, self.left, self.bottom, self.right]
            if slot is not None
        ]
