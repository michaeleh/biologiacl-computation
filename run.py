import matplotlib.pyplot as plt

from question2.automata import generate_population, next_generation, population, get_generation_number, happiness_value
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

    for i in range(0, 20):
        sample_happiness()
        next_generation()
    sample_happiness()

    print(len(population))
    start_gui()

    plot_happiness_per_generation()
