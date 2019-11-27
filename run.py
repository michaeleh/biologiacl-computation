import matplotlib.pyplot as plt

from automata import generate_population, next_generation, population, singles_left, happiness_per_gen
from config import SKIP_TO_THE_END
from gui import start_gui


def plot_happiness_per_generation():
    plt.title('Happiness Per Generation')
    plt.xlabel('Generation')
    plt.ylabel('Happiness')
    plt.plot(happiness_per_gen.keys(), happiness_per_gen.values())
    plt.show()


if __name__ == "__main__":
    generate_population()
    i = 0
    while SKIP_TO_THE_END:
        i += 1
        next_generation()
        if not singles_left():
            break

    start_gui()

    print(len(population))

    plot_happiness_per_generation()
