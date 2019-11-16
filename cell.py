import random
from enum import Enum

from question2.consts import WIDTH, HEIGHT


def get_cell_radius(x, y, r=1):
    indexes = []
    start = -r
    end = r + 1
    for i in range(start, end):
        for j in range(start, end):
            if 0 <= x + i < WIDTH and 0 <= y + j < HEIGHT:
                indexes.append((x + i, y + j))

    return indexes


class Cell:

    def __init__(self) -> None:
        self.value = ''
        self.x = 0
        self.y = 0

    def get_color(self):
        return Sex.Other.value

    def move(self, neighbors):
        possible_indexes = get_cell_radius(self.x, self.y)
        for x, y in neighbors.keys():
            radius = get_cell_radius(x, y)
            for index in radius:
                if index in possible_indexes:
                    possible_indexes.remove(index)
        if possible_indexes:
            x, y = random.sample(possible_indexes, 1)[0]
            self.x = x
            self.y = y


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

    def move(self, n):
        pass


class Sex(Enum):
    Male = "lightblue"
    Female = "pink"
    Couple = "green"
    Other = "white"
