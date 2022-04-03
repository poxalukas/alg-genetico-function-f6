import numpy as np


#Seleção do metodo da roleta
def selection(pop_bin, fitness, pop_size):
    proxima_geracao = list()

    P = [f/sum(fitness) for f in fitness]  #seleção da prob
    index = list(range(int(len(pop_bin))))
    index_selected = np.random.choice(index,size=pop_size,replace=False,p=P)

    s=0
    for j in range(pop_size):
        proxima_geracao.append(pop_bin[index_selected[s]])
        s+=1
    #print(proxima_geracao)
    return proxima_geracao
