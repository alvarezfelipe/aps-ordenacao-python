# import string
import random
import urllib.request

#Lendo lista de palavras do site
site = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
response = urllib.request.urlopen(site)
texto = response.read().decode()
palavras = texto.splitlines()

# #criando lista de palavras embaralhadas
listaEmbaralhada = []
for i in range(10):
    #print(random.choice(palavras))
    listaEmbaralhada.append(random.choice(palavras))
#print(listaEmbaralhada)

lista2 = []
for l in listaEmbaralhada:
    lista2.append(l.upper())
print(lista2)   

#print(type(palavras))