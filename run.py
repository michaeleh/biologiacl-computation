from question2.automata import generate_population, next_generation, population
from question2.gui import start_gui

if __name__ == "__main__":
    generate_population()
    start_gui()
    for i in range(0, 1000):
        next_generation()
    print(len(population))
