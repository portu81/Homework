class turtle(object):
    def __init__(self, x, y, s):
        self.s = s
        self.x = x
        self.y = y

    def go_up(self):
        self.y += self.s
        print(self.x, self.y, sep=', ')

    def go_down(self):
        self.y -= self.s
        print(self.x, self.y, sep=', ')

    def go_left(self):
        self.x -= self.s
        print(self.x, self.y, sep=', ')

    def go_right(self):
        self.x += self.s
        print(self.x, self.y, sep=', ')

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s == 1:
            raise ValueError("Ход не может быть равен 0 или отрицательным.")
        else:
            self.s -= 1

    def count_moves(self, x2, y2):
        self.x = self.x + (x2 - self.x)
        self.y = self.y + (y2 - self.y)
        print(self.x, self.y, sep=', ')

a = turtle(1, 1, 2)
a.evolve()
a.go_up()
