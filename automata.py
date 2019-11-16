import random

from question2.cell import Person, Sex, Couple
from question2.config import *

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


def get_neighbors(current_population, person, radius=2):
    """
    builds dictionary of neighbors from current population to that person
    :param radius: how far to search
    :param current_population: dictionary of the current population
    :param person: to find its neighbors
    :return: dictionary of (i,j)->neighbor
    """
    start = -radius
    end = radius + 1
    x, y = person.x, person.y
    neighbors = {}
    for i in range(start, end):
        for j in range(start, end):
            if (i != 0 or j != 0) and (x + i, y + j) in current_population:
                neighbors[(x + i, y + j)] = (current_population[(x + i, y + j)])
    return neighbors


def update_potential_partner(current_population):
    """
    create dictionary of couples who both wants each other
    :param current_population: population of people
    :return: dictionary of couples
    """
    singles = [p for p in current_population.values() if p.sex != Sex.Couple]  # all singles
    potential_couples = {}

    for person in singles:
        best_match = person.best_match(get_neighbors(current_population, person, radius=1))  # best match for couple
        potential_couples[person] = best_match

    couples = {}
    added = []
    # add only one of them
    for person1, person2 in potential_couples.items():
        if (person2 in potential_couples) and (person1 not in added):  # partner is here
            if potential_couples[person2] == person1:  # mutual desire
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

    current_population = breakup_couples_if_necessary(current_population)  # swap couples
    potential_couples = update_potential_partner(current_population)  # new couples

    for index, person in current_population.items():
        if person in potential_couples:
            population[(person.x, person.y)] = Couple(person, potential_couples[person])
        elif person not in potential_couples.values():
            person.move(get_neighbors(current_population, person))  # move regular non empty cells
            population[(person.x, person.y)] = person


def breakup_couples_if_necessary(current_population):
    """
    search for better option in neighbors for each couple
    :param current_population:
    :return: new population with swapped couples
    """
    couples = [couple for couple in current_population.values() if couple.sex == Sex.Couple]
    for couple in couples:
        neighbors = get_neighbors(current_population, couple, radius=1)
        for neighbor in neighbors.values():
            couple, neighbor = swap_if_better(couple, neighbor)  # swap if better
            current_population[(couple.x, couple.y)] = couple
            current_population[(neighbor.x, neighbor.y)] = neighbor
    return current_population


def happiness_value():
    happiness = 0
    for person in population.values():
        happiness += person.happiness_val()

    return happiness


def get_generation_number():
    global generations
    return generations


def swap_if_better(couple, p):
    """
    checks if swapping gives a better happiness value
    :param couple:
    :param p: couple or person to swap
    :return: new or same (coupe,p) tuple
    """
    if not CAN_BREAKUP:
        return couple, p

    current_val = couple.happiness_val() + p.happiness_val()
    p = couple.swap(p)
    new_val = couple.happiness_val() + p.happiness_val()
    if new_val > current_val:
        return couple, p
    p = couple.swap(p)
    return couple, p


def singles_left():
    return len([p for p in population.values() if p.sex != Sex.Couple]) > 0  # still singles found
