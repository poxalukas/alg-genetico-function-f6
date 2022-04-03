from random import choices

def gerar_genoma(length: int):
    choices_selected = choices([0, 1], k=length)
    return choices_selected


#Cria a população de 44bits para real
def inicializa_pop(bounds,bits,genoma,pop_size):
    lower_x_boundary, upper_x_boundary = bounds[0]
    lower_y_boundary, upper_y_boundary = bounds[1]
    half_genome = bits/2
    population = []
    population_bit = []


    for i in range(pop_size):
        cromossomox = ""
        cromossomoy = ""

        for j in range(len(genoma)):
            if j < half_genome:
                cromossomox += str(genoma[j])

            else:
                cromossomoy += str(genoma[j])

        individuo_bit = {
            "x": cromossomox,
            "y": cromossomoy
        }
        if cromossomox != '' and cromossomoy != '':
            b = int(cromossomox,2)
            cromossomox_float = float(b)
            c = (int(cromossomoy, 2))
            cromossomoy_float = float(c)
            if type(cromossomox_float) == float and type(cromossomoy_float) == float:
                cromossomox_decimal = cromossomox_float * float((upper_x_boundary - lower_x_boundary) / (pow(2, half_genome) - 1)) + float(lower_x_boundary)
                cromossomoy_decimal = cromossomoy_float * float((upper_y_boundary - lower_y_boundary) / (pow(2, half_genome) - 1)) + float(lower_y_boundary)
                individuo = {
                    "x": cromossomox_decimal,
                    "y": cromossomoy_decimal
                }
                population.append(individuo)
                population_bit.append(individuo_bit)

                genoma = gerar_genoma(bits)

            else:
                break
    return population,population_bit




