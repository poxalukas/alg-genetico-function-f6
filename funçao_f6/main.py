from numpy.random import rand, randint
import numpy as np
import matplotlib.pyplot as plt
from novagen import novagen
from populacao import inicializa_pop
from populacao import gerar_genoma
from funcao import f6
from selecao import selection
from crossover import crossover
from mutacao import mutation
from novagen import novagen

# Parametros de entrada do Algoritmo Genetico
bounds = [[-100, 100], [-100, 100]]         #range do numero real
qtdgeracoes = 500                    #quantidade de geraçoes
bits = 44                                   #numero de bits do Genoma
pop_size = 100                                 #tamanho da populaçao
crossover_rate = 0.65                      #taxa de crossover
mutation_rate = 0.08                     #tava de mutaçao
genoma = []                                 #lista dos genomas separados por virgula


# ---------------------------------Programa Principal-----------------------------------------------#
genoma = gerar_genoma(bits)#gera um genoma aleatorio
pop_real,pop_bin = inicializa_pop(bounds,bits,genoma,pop_size)#gera a pop binaria e real passando o range, os bits, o genoma gerado e o tamano da populaçao
offspring = []#auxiliar 
best_fitness = []#contem os melhores fitness
lista_genoma= []#lista de genomas
lista_medias = []#medias de fitness
fitness=[]      #contem os fitness
omelhor=[]      #contem os melhores fitness de cada geraçao

for gen in range(qtdgeracoes):
        print("geraçao - ",gen)

        #funçao fitness aplicada
        # for d in pop_real:    
        #         result=f6(d)
        #         fitness.append(result)
        
        fitness=f6(pop_real)


        index=np.argmax(fitness)
        media=np.mean(fitness)
        melhor_fitness_atual=fitness[index]
        melhor_binario_atual=pop_bin[index]
        melhor_real_atual=pop_real[index]
        omelhor.append(melhor_fitness_atual)
        lista_medias.append(media)

        #seleciona o valor maximo em real
        best_fitness.append(max(fitness))

                #realiza crossover dos pares
        pop_bin=crossover(pop_bin, crossover_rate,bits)
                #realiza mutaçao do pares
        pop_bin=mutation(pop_bin, mutation_rate)

                 #seleçao por roleta
        pop_bin = selection(pop_bin,fitness,pop_size)

        for p in pop_bin:
                offspring.append(p)

        for _ in offspring:
                genoma = ''.join(str(_['x'])+str(_['y']))
                lista_genoma.append(genoma)

        #seleciona o valor maximo em real
        best_fitness.append(max(fitness))

        pop_bin=[]
        pop_real=[]
        fitness=[]
        num_real=[]
        num_bin=[]
        offspring=[]

        for p in lista_genoma:
               novagen_real,novagen_bin=novagen(bounds,bits,p)
               pop_real=np.concatenate((pop_real,novagen_real))
               pop_bin=np.concatenate((pop_bin,novagen_bin))

        lista_genoma=[]
        
        #elitismo
        aleatorio=randint(0,pop_size-1)
        pop_bin[aleatorio]=melhor_binario_atual
        pop_real[aleatorio]=melhor_real_atual
        # print(pop_real)
        # print(len(pop_real)) 
        print("Melhor em binario:",melhor_binario_atual,"\nMelhor em real:",melhor_real_atual,"\nFitness:",melhor_fitness_atual)
        print("Media Fit: ",media,"\n")
 
plt.plot(lista_medias)
plt.plot(omelhor)
plt.xlabel('Fitness', fontsize=15)
plt.ylabel('Quantidade de Gerações', fontsize=15)
plt.title('Maximizando Funçao F6')
plt.legend(['Media de Fitness de cada geraçao','Melhor Fitness de cada geraçao'], fontsize=6,loc='lower right')
axes = plt.gca()
axes.yaxis.grid(b=True, color='black', alpha=0.3, linestyle='-.', linewidth=1)
plt.show()


    
