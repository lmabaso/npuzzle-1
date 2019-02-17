class Goal:

    def __init__(self, size):
        self.size = size
        self.len = size * size
        self.num = 1
        self.row = 0
        self.col = -1
        self.border_up = 1
        self.border_down = size - 1
        self.border_left = 0
        self.border_right = size - 1
        self.generate_puzzle()
        self.generate_hash()

    def assign_num(self):
        index = self.row * self.size + self.col
        if self.num == self.len:
            self.puzzle[index] = 0
            return (True)
        self.puzzle[index] = self.num
        self.num += 1
        return (False)

    def move_right(self):
        while self.col < self.border_right:
            self.col += 1
            if self.assign_num():
                return (True)
        self.border_right -= 1
        return (False)

    def move_down(self):
        while self.row < self.border_down:
            self.row += 1
            if self.assign_num():
                return (True)
        self.border_down -= 1
        return (False)

    def move_left(self):
        while self.col > self.border_left:
            self.col -= 1
            if self.assign_num():
                return (True)
        self.border_left += 1
        return (False)

    def move_up(self):
        while self.row > self.border_up:
            self.row -= 1
            if self.assign_num():
                return (True)
        self.border_up += 1
        return (False)

    def generate_puzzle(self):
        self.puzzle = [None for i in range(self.len)]
        while True:
            if self.move_right():
                return
            if self.move_down():
                return
            if self.move_left():
                return
            if self.move_up():
                return

    def generate_hash(self):
        self.hash = {}
        for i, val in enumerate(self.puzzle):
            self.hash[val] = (int(i / self.size), i % self.size)