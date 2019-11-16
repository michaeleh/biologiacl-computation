import matplotlib.pyplot as plt

from question2.automata import generate_population, next_generation, population, get_generation_number, happiness_value, \
    singles_left
from question2.config import SKIP_TO_THE_END
from question2.gui import start_gui


def plot_happiness_per_generation():
    plt.title('Happiness Per Generation')
    plt.xlabel('Generation')
    plt.ylabel('Happiness')
    plt.plot(happiness_per_gen.keys(), happiness_per_gen.values())
    plt.show()


def sample_happiness():
    global generation_number, happy_value
    generation_number = get_generation_number()
    happy_value = happiness_value()
    happiness_per_gen[generation_number] = happy_value


if __name__ == "__main__":
    happiness_per_gen = {}
    generate_population()

    while SKIP_TO_THE_END:
        sample_happiness()
        next_generation()
        if not singles_left():
            break
    sample_happiness()

    start_gui()

    print(len(population))

    plot_happiness_per_generation()
