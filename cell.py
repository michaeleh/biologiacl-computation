import random
from enum import Enum

from question2.consts import WIDTH, HEIGHT


class Cell:

    def __init__(self) -> None:
        self.value = ''
        self.x = 0
        self.y = 0

    def get_color(self):
        return Sex.Other.value

    def move(self, neighbors):
        possible_moves = []
        max_h, max_w, min_h, min_w = self.get_ranges()
        for i in range(min_w, max_w):
            for j in range(min_h, max_h):
                if (self.x + i, self.y + j) not in neighbors:
                    possible_moves.append((i, j))
        if len(possible_moves) > 0:
            i, j = random.sample(possible_moves, 1)[0]
            self.x += i
            self.y += j

    def get_ranges(self):
        min_w = min_h = -1
        max_w = max_h = 2
        if self.x == 0:
            min_w = 0
        if self.y == 0:
            min_h = 0
        if self.x == WIDTH - 1:
            max_w = 0
        if self.y == HEIGHT - 1:
            max_h = 0
        return max_h, max_w, min_h, min_w


class Person(Cell):
    def __init__(self, x, y, sex) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.sex = sex
        self.value = random.randint(0, 100)
        self.happiness_val = 0

    def get_color(self):
        return self.sex.value

    def best_match(self, neighbor):
        min_val = 101
        best_match = None
        for p in neighbor.values():
            if p.sex != self.sex:
                couple_val = abs(p.value - self.value)
                if couple_val < min_val:
                    min_val = couple_val
                    best_match = p
        return best_match


class Couple(Cell):
    def __init__(self, man, woman) -> None:
        super().__init__()
        self.man = man
        self.x = man.x
        self.y = man.y
        self.woman = woman
        self.value = abs(man.value - woman.value)
        self.sex = Sex.Couple
        self.happiness_val = 100 - self.value

    def get_color(self):
        return self.sex.value

    def best_match(self):
        return None


class Sex(Enum):
    Male = "lightblue"
    Female = "pink"
    Couple = "green"
    Other = "white"
