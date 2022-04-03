# alg-genetico-function-f6

Implementaçao do algoritmo genetico em py de maximizaçao F6, proposto na aula de Inteligencia artificial pelo professor Celso da UFG.

Representação
● Binária codificando real
● 2 Variáveis: x, y
● Domínio: x,y ∈ [-100, +100]
● Precisão: 4 a 5 casas decimais
● Ki=22  total de 44 bits

Exemplo
● Cromossoma:
00001010000110000000011000101010001110111011
● Dividido em x e y:
0000101000011000000001 1000101010001110111011
● Convertidos para base 10:
165377 e 2270139
● Multiplicados por: 200/222-1
7,885791751335085 e 108,24868875710696
● Somados a mín:
x=-92,11420824866492 e y=8,248688757106959
● Aplicados a F6(x,y):
F6(x,y)=0,5050708


O algoritmo esta dividido para que seja feito uma melhora visual no codigo;

O intuito do desafio era criar um algoritmo genenetico que gere uma populaçao de tamanho n(pop_size), e populasse com numeros aleatorios de -100 a 100;
Cada individuo da populaçao tem um tamanho fixo de bits, onde serão feitos operaçoes elementares de elitismo, mutaçao e crossover, afim de garantir que a funçao F6 seja cumprida e seguindo os conceitos de Algoritmo genetico

populacao.py
A funçao novagen.py, gera a populaçao inicial, recebendo um genoma aleatorio de 0 e 1's e os bounds(nese caso de -100 a 100) e retorna tuplas de x e y, sendo tanto uma populaçao binaria, quanto uma populaçao real;

funcao.py
Apos gerar a nova populaçao, se passa ela pra funcao.py, onde calculamos o fit, e dentro da funçao.py que sao feitos os calculos da nossa funçao

F6(x,y) = 0,5 - (((sen √ x² + y² )2 - 0,5)/(1,0 + 0,001 (x² + y² ))²)

com as seguintes caracteristicas:
Uma única solução ótima: F6(0,0)=1
Difícil de otimizar: vários mínimos locais

apos efetuar as operaçoes de f6, armazenamos na variavel fitness, e dela tiramos:
o indice do melhor fitness
a media dos fitness
o melhor fitness, tanto em real quanto em binario 

e armazenamos em uma lista o melhor fitness atual, em real e em binario, a media dos fitness atuais, e tambem o melhor fitness

entao passamos a populaçao binaria para a funçao de crossover com intuito de criar filhos melhores da populaçao atual

crossover.py
recebe a populaçao binaria, a taxa de crossover e a quantidade de bits
cria uma variavel aleatoria e, se ela for menor que a taxa de crossover faz-se um corte aleatorio nos cromossomos x e y e entao junta o corpo de x a calda de y onde foi efetuado o corte e vice versa e entao retorna essa lista de novos cromossomos

é então retornado a nova populaçao binaria, e entao enviamos essa populaçao para mutaçao onde sao trocados aleatoriamente genes dos nossos cromossomos

mutacao.py
recebendo a populaçao binaria e a taxa de mutaçao o algoritmo pega o cromossomo x e y e o envia a funçao mutacao, e se a taxa de mutaçao for maior que o numero aleatorio gerado, cp recebe o indice aleatorio de onde deve ser feito a alteraçao de gene e então e efetuado a troca por 0 ou 1, e essa lista nova e retornada ao programa principal

ao retornar já com a nova pop bin com crossover e tambem mutada, utilizamos o metodo da roleta para sortear os pais que então farao parte da nova geraçao 

selecao.py
essa funçao recebe a populaçao binaria, os resultados da funçao que estao em fitness, e o tamanho da populaçao
como o metodo da roleta sugere, é gerado uma lista de probabilidades P, onde é efetuado a divisao do fitness pela soma total dos fitness
P = [f/sum(fitness) for f in fitness]
é gerado tambem um index que e uma lista de 0 a tamanho tamanho da pop-1
tendo essas duas variaveis agora fazemos o sorteio dos pais da proxima geraçao:
    index_selected = np.random.choice(index,size=pop_size,replace=False,p=P)
agora com a lista de index selecionados, o que fazemos entao é adicionar a nossa proxima geraçao os pais escolhidos, tendo possibilidades de mesmos pais serem repetidos  

voltando ao programa principal, é entao gerado uma offspring da populaçao para armazenar todos os x's e y's, e apos isso juntamos x e y para gerar um novo genoma de 44 bits(ou tamanho de bits)
apos isso entao limpamos as listas pra nao ficar armazenando variaveis desnecessarias;

agora para cada p de lista_genomas criamos uma nova populaçao pela funçao novagen.py que é uma funçao similar a populacao.py, porem feito somente para gerar novas populaçoes e entao concatenamos com a pop_bin e pop_real(por problemas de implementaçao das quais desconheco pois nao domino py, nao conseguia passa diretamente para essas funçoes)

apos gerar a nova geraçao, entao fazemos o elitismo, que era o melhor par de inidividuos da fitness na geraçao passada, e em uma posiçao aleatoria adicionamos tanto o binario quanto o real e imprimimos o resultados atuais
=================================================================================================================================================
apos finalizar o laço de quantidade de geraçoes, plotamos  um grafico com nossos resultados obtidos
