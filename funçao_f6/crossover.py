from numpy.random import rand, randint


def crossover(pop_bin, crossover_rate,bits):
    offspring = []
    for i in range(int(len(pop_bin))):
        px = pop_bin[i]['x']  # parent 1
        py = pop_bin[i]['y']  # parent 2
        rand_variable = rand()
        if rand_variable < crossover_rate: 

            cp = randint(1,(bits/2)-1)
            c1 = px[:cp] + py[cp:]
            c2 = py[:cp] + px[cp:]
            c = {
                'x': c1,
                'y': c2
            }
            offspring.append(c)
        else:
            c = {
                'x':px,
                'y':py
            }
            offspring.append(c)

    return offspring