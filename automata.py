import random

from question2.cell import Person, Sex, Couple
from question2.consts import *

population = {}
generations = 0


def generate_indexes(num):
    """
    generate random indexes (i,j) pairs in range of width, height
    :param num: number of indexes to randomly pick
    :return: array with tuples of (i,j) randomly selected on grid
    """
    places = []
    for i in range(WIDTH):
        for j in range(HEIGHT):
            places.append((i, j))

    xy = random.sample(places, num)
    return xy


def generate_population(num_of_men=50, num_of_women=50):
    """
    generate population of {@num_of_men} men and {@num_of_women} women
    located in random position on the grid
    :param num_of_men: how much men are in the population
    :param num_of_women: how much women are in the population
    """

    def add_person(i, xy):
        """
        adding a person to the population
        :param i: index of the person
        :param xy: tuple of (i,j)
        """
        x = xy[i][0]
        y = xy[i][1]
        sex = Sex.Male if i < num_of_men else Sex.Female
        population[(x, y)] = Person(x, y, sex)

    population.clear()
    xy = generate_indexes(num_of_men + num_of_women)
    for i in range(num_of_men + num_of_women):
        add_person(i, xy)


def get_neighbors(current_population, person):
    """
    builds dictionary of neighbors from current population to that person
    :param current_population: dictionary of the current population
    :param person: to find its neighbors
    :return: dictionary of (i,j)->neighbor
    """
    x, y = person.x, person.y
    neighbors = {}
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0) and (x + i, y + j) in current_population:
                neighbors[(x + i, y + j)] = (current_population[(x + i, y + j)])
    return neighbors


def update_potential_partner(current_population):
    """
    create dictionary of couples who both wants each other
    :param current_population: population of people
    :return: dictionary of couples
    """
    singles = [p for p in current_population.values() if p.sex != Sex.Couple]
    potential_couples = {}
    for person in singles:
        best_match = person.best_match(get_neighbors(current_population, person))
        potential_couples[person] = best_match

    couples = {}
    added = []
    for person1, person2 in potential_couples.items():
        if (person2 in potential_couples) and (person1 not in added):
            if potential_couples[person2] == person1:
                couples[person1] = person2
                added.append(person2)
    return couples


def next_generation():
    """
    moves all the cells and progress generation
    """
    global generations
    generations += 1
    current_population = population.copy()
    population.clear()

    couples = update_potential_partner(current_population)

    for index, person in current_population.items():
        if person in couples:
            population[(person.x, person.y)] = Couple(person, couples[person])
        elif person not in couples.values():
            move(current_population, person)


def move(current_population, person):
    """
    move cell
    :param current_population:
    :param person:
    :return:
    """
    x, y = person.x, person.y
    person.move(get_neighbors(current_population, person))
    new_x = person.x
    new_y = person.y
    if (new_x, new_y) not in population:
        population[(new_x, new_y)] = person
    else:
        person.x, person.y = x, y
        population[(x, y)] = person


def happiness_value():
    happiness = 0
    for person in population.values():
        happiness += person.happiness_val
    return happiness


def get_generation_number():
    global generations
    return generations
