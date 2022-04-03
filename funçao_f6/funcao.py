import math

from matplotlib import offsetbox

def f6(pop_real):

    lista_fitness = []
    for i in range(int(len(pop_real))):
        x = pop_real[i]['x']  # parent 1
        y = pop_real[i]['y']  # parent 2
        x_y_pow = float(x ** 2 + y ** 2)
        square_of_pow = math.sqrt(x_y_pow)
        sin_pow = (math.sin(square_of_pow) ** 2)
        fraction = (((sin_pow) - (0.5))) / (((1 + (float(0.001) * (x_y_pow)))) ** 2)
        result = (0.5) - fraction
        lista_fitness.append(result)

    return lista_fitness