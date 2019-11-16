from tkinter import *

from question2.automata import next_generation, population, happiness_value, get_generation_number
from question2.cell import Cell
from question2.config import *

HAPPINESS = 'happiness'
GENERATIONS = 'generations'

entries = {}
labels = {}


def draw_grid():
    """
    draws grid of white empty cells and then draws the people in their positions
    """

    labels[GENERATIONS].configure(text=f"generations: {get_generation_number()}")
    labels[HAPPINESS].configure(text=f"happiness: {happiness_value()}")

    for row in range(WIDTH):
        for col in range(HEIGHT):
            cell = Cell()
            entries[(row, col)].configure(bg=cell.get_color())
            entries[(row, col)].delete(0, END)

    for person in population.values():
        entries[(person.x, person.y)].configure(bg=person.get_color())
        entries[(person.x, person.y)].delete(0, END)
        entries[(person.x, person.y)].insert(0, person.value)


def start_gui():
    """
    initiate gui engine and build empty grid
    """
    root = Tk()
    entries.clear()
    Button(root, text="Next Gen", command=update_grid, bg='purple', fg='white').grid(row=WIDTH // 2, column=HEIGHT)
    generation_number = get_generation_number()
    happy_value = happiness_value()
    gen_label = Label(root, text=f"generations: {generation_number}")
    gen_label.grid(row=0, column=HEIGHT)
    happiness_label = Label(root, text=f"happiness: {happy_value}")
    happiness_label.grid(row=1, column=HEIGHT)
    labels[GENERATIONS] = gen_label
    labels[HAPPINESS] = happiness_label
    for row in range(WIDTH):
        for col in range(HEIGHT):
            cell = Cell()
            entry = Entry(root, width=3, text=cell.value, bg=cell.get_color())
            entry.grid(row=row, column=col)
            entries[(row, col)] = entry

    draw_grid()
    mainloop()


def update_grid():
    next_generation()
    draw_grid()
