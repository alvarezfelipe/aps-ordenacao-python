#Classe auxiliar contendo todas as funções que serão utilizadas

#Imports
import random
import time
import urllib.request
import shutil

listaDeDados = []
listaDePalavras = []

#Gerando números aleatórios e salvando na lista
def criaLista(qtde): 
    # Laço de repetição na quantidade informada pelo usuário
    # A geração dos números é feita pela função RANDINT(MÍN, MÁX)  
    for i in range(qtde):
        listaDeDados.append(random.randint(0 , 1000000))
    print(f'A lista gerada aleatoriamente foi \n {listaDeDados} \n')

#Gerando lista de palavras aleatórias
def listaPalavras(qtde):
    # Utilização da URLLIB para leitura de dados
    # Base de dados com mais de 247mil palavras em PT-BR conhecidas
    site = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt' 
    response = urllib.request.urlopen(site)
    texto = response.read().decode()
    palavras = texto.splitlines()    

    # Laço de repetição na quantidade informada pelo usuário
    # A função CHOICE seleciona palavras aleatórias dentro de uma lista
    for i in range(qtde):    
        listaDePalavras.append(random.choice(palavras))
    
    # Laço utilizado para colocar todas as palavras da lista em LETRAS MAIÚSCULAS
    for palavra in listaDePalavras:
        listaDeDados.append(palavra.upper())
    print(f'A lista gerada aleatoriamente foi \n {listaDeDados} \n')

#Apagando a lista
def apagaLista():
    if not listaDeDados:
        print('A lista já está vazia. \n')
    else:
        listaDeDados.clear()
        print('Lista apagada com sucesso! \n')

# *-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-*
#Funções de Ordenação
#Método Bubble
def ordBubble(lista):
    qtdeElementos = len(lista) - 1
    ordenar = False

    while not ordenar:
        ordenar = True
        for i in range(qtdeElementos):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenar = False
    
    print(f'Lista ordenada pelo Bubble: \n {lista}')

#Método Insertion
def ordInsertion(lista):
    for i in range(1, len(lista)):
        posicaoLista = i
        valor = lista[i]

        while posicaoLista > 0 and lista[posicaoLista -1] > valor:
            lista[posicaoLista] = lista[posicaoLista -1]
            posicaoLista = posicaoLista - 1
        lista[posicaoLista] = valor
    
    print(f'Lista ordenada pelo Insertion: \n {lista}')

#Método Merge
def ordMerge(lista):
    def merge(novaLista):
        if len(novaLista) > 1:
            meio = len(novaLista) // 2
            ladoEsquerdo = novaLista[:meio]
            ladoDireito = novaLista[meio:]

            merge(ladoEsquerdo)
            merge(ladoDireito)

            i = 0
            j = 0
            k = 0

            while i < len(ladoEsquerdo) and j < len(ladoDireito):
                if ladoEsquerdo[i] < ladoDireito[j]:
                    novaLista[k] = ladoEsquerdo[i]
                    i += 1
                else:
                    novaLista[k] = ladoDireito[j]
                    j += 1
                k += 1

            while i < len(ladoEsquerdo):
                novaLista[k] = ladoEsquerdo[i]
                i += 1
                k += 1

            while j < len(ladoDireito):
                novaLista[k] = ladoDireito[j]
                j += 1
                k += 1

    merge(lista)    
    print(f'Lista ordenada pelo Merge: \n {lista}')

#Método Quick
def ordQuick(lista):
    def particao(novaLista, menor, maior):
        i = (menor - 1)
        pivo = novaLista[maior]

        for j in range(menor, maior):
            if novaLista[j] <= pivo:
                i += 1
                novaLista[i], novaLista[j] = novaLista[j], novaLista[i]
        novaLista[i+1], novaLista[maior] = novaLista[maior], novaLista[i+1]
        return i + 1
    
    def metodoQuick(novaLista, menor, maior):
        if len(novaLista) == 1:
            return novaLista
        if menor < maior:
            pi = particao(novaLista, menor, maior)
            metodoQuick(novaLista, menor, pi - 1)
            metodoQuick(novaLista, pi + 1, maior)
        
    metodoQuick(lista, 0, len(lista) - 1)
    print(f'Lista ordenada pelo Quick: \n {lista}')

# *-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-**-*-*-*-*-*-*
#Comparando as funções
def verificaQuick(lista):
    novaLista = lista.copy()
    abreTempo = time.time()
    ordQuick(novaLista)
    fechaTempo = time.time()
    total = (fechaTempo - abreTempo)
    print(f'Tempo total para ordenação no método Quick: {total} segundos.')
    separador()

def verificaBubble(lista):
    novaLista = lista.copy()
    abreTempo = time.time()
    ordBubble(novaLista)
    fechaTempo = time.time()
    total = (fechaTempo - abreTempo)
    print(f'Tempo total para ordenação no método Bubble: {total} segundos.')
    separador()

def verificaMerge(lista):
    novaLista = lista.copy()
    abreTempo = time.time()
    ordMerge(novaLista)
    fechaTempo = time.time()
    total = (fechaTempo - abreTempo)
    print(f'Tempo total para ordenação no método Merge: {total} segundos.')
    separador()

def verificaInsertion(lista):
    novaLista = lista.copy()
    abreTempo = time.time()
    ordInsertion(novaLista)
    fechaTempo = time.time()
    total = (fechaTempo - abreTempo)
    print(f'Tempo total para ordenação no método Insertion: {total} segundos.')
    separador()

def separador():
    tamanho_terminal = shutil.get_terminal_size((180, 20))
    colunas = tamanho_terminal.columns    
    print('-' * colunas)