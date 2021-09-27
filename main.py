# Desenvolvimento de algortimo de ordenação de valores

# Elaborado por FELIPE ALVAREZ DOS SANTOS e JOÃO HENRIQUE BENATTI COIMBRA

# Imports
import funcoes

qtdeDados = 0

# Input de Dados pelo usuário
# qtdeDados = int(input('Quantos itens quer adicionar na lista? '))

while True:
    print('''
    *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
    * Sistema básico para Ordenação de Dados*
    *                                       *
    * Escolha uma opção abaixo:             *
    * 1 --> Criar Lista Numérica            *
    * 2 --> Criar Lista Palavras            *
    * 3 --> Apagar a Lista                  *
    * 4 --> Ordenação pelo Bubble           *
    * 5 --> Ordenação pelo Insertion        *
    * 6 --> Ordenação pelo Merge            *
    * 7 --> Ordenação pelo Quick            *
    * 8 --> Comparando os métodos           *
    * 9 --> Sair do Sistema                 *
    *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
    ''')

    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        qtdeDados = int(input('Quantos itens quer adicionar na lista? '))
        funcoes.criaLista(qtdeDados)
        continue
    elif opcao == '2':
        qtdeDados = int(input('Quantos itens quer adicionar na lista? '))
        funcoes.listaPalavras(qtdeDados)
        continue
    elif opcao == '3':
        funcoes.apagaLista()
        continue
    elif opcao == '4':
        if not funcoes.listaDeDados:
            print('Lista está vazia. Crie uma antes de ordenar os dados')
        else:
            funcoes.verificaBubble(funcoes.listaDeDados)
        continue
    elif opcao == '5':
        if not funcoes.listaDeDados:
            print('Lista está vazia. Crie uma antes de ordenar os dados')
        else:
            funcoes.verificaInsertion(funcoes.listaDeDados)
        continue
    elif opcao == '6':
        if not funcoes.listaDeDados:
            print('Lista está vazia. Crie uma antes de ordenar os dados')
        else:
            funcoes.verificaMerge(funcoes.listaDeDados)
        continue
    elif opcao == '7':
        if not funcoes.listaDeDados:
            print('Lista está vazia. Crie uma antes de ordenar os dados')
        else:
            funcoes.verificaQuick(funcoes.listaDeDados)
        continue
    elif opcao == '8':
        if not funcoes.listaDeDados:
            print('Lista está vazia. Crie uma antes de ordenar os dados')
        else:
            print('\n ... Comparando os métodos de ordenação ... \n')
            funcoes.verificaBubble(funcoes.listaDeDados)
            funcoes.verificaInsertion(funcoes.listaDeDados)
            funcoes.verificaMerge(funcoes.listaDeDados)
            funcoes.verificaQuick(funcoes.listaDeDados)
        continue
    elif opcao == '9':
        print('... Encerrando o programa ...')
        break
    else:
        print('Opção inválida')
