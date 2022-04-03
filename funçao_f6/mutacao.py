from numpy.random import rand, randint


def mutation(pop_bin, mutation_rate):
    offspringX = list()
    offspringY = list()
    populacao_mutada = []
    for i in range(int(len(pop_bin))):
        px = pop_bin[i]['x'] #parent X
        py = pop_bin[i]['y'] #parent y
        cx = mutacao(px,mutation_rate,offspringX)
        cy = mutacao(py,mutation_rate,offspringY)
        individual_bit_mutaded = {
            "x": cx[i],
            "y": cy[i]
        }
        populacao_mutada.append(individual_bit_mutaded)
    return populacao_mutada

def mutacao(p1,mutation_rate,offspring):
    if rand() < mutation_rate:
        cp = randint(0, len(p1))  # gera gene aleatorio
        c1 = p1
        c = list(c1)

        if c[cp] == "1":
            c[cp] = "0"  # troca bit
        else:
            c[cp] = "1"
        c_aux = ''.join([str(elem) for elem in c])
        offspring.append(c_aux)
    else:
        offspring.append(p1)
    return offspring