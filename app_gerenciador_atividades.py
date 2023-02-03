from sql import *
from os import system


resposta = ''
while resposta != 'N':    
    opcao = input('''
1 - Novo cadastro
2 - Visualizar atividades
3 - Visualizar categorias
4 - Atualização de status
5 - Atualização de atividades ou categorias
6 - Exclusão de atividades ou categorias\n
Qual operação sera feita?\n--> ''')
    opcao =  opcao_valida(opcao)
    if opcao == 1:
        system('clear')
        opcao = input('''\nQual o novo cadastro?
    1 - Cadastrar nova atividade
    2 - Cadastrar nova categoria:\n--> ''')
        opcao =  opcao_valida(opcao)
        if opcao == 1:
            novo_cadastro('atividade')
        elif opcao == 2:
            novo_cadastro('categoria')
        else:
            print('Opção invalida, tente novamente')
        resposta = ciclo_nova_operacao()
    
    elif opcao == 2:
        system('clear')
        opcao = input('''1° - Mostrar todas as atividades\n2° - Filtrar atividades\n--> ''')
        opcao =  opcao_valida(opcao)
        if opcao == 1:
            pesquisa_dados('atividades', None, None, None)
            
        elif opcao == 2:
            opcao = input('''\nQual filtro utilizar:
    1° - Nome
    2° - Data
    3° - Catedoria
    4° - Status\n--> ''')
            opcao =  opcao_valida(opcao)
            if opcao == 1:
                where = 'nome'
            elif opcao == 2:
                where = 'data'
            elif opcao == 3:
                where = 'categoria'''
            else:
                where = 'status'
            parametro = str(input(f'''Digite o valor de {where}: ''')).strip().capitalize()
            pesquisa_dados('atividades', where, parametro, None )
        else:
            print('Opção invalida, tente novamente')
        resposta = ciclo_nova_operacao()

    elif opcao == 3:
        pesquisa_dados('categoria', None, None, None)
        resposta = ciclo_nova_operacao()

    elif opcao == 4:
        status()
        resposta = ciclo_nova_operacao()

    elif opcao == 5:
        system('clear')
        tabela = input('''O que deseja atualizar?
    1 - Atualizar atividade
    2 - Atualizar categoria\n--> ''')
        opcao =  opcao_valida(opcao)
        if opcao == 1:
            atualizar_dados('atividade')
        elif opcao == 2:
            atualizar_dados('categoria')
        else:
            print('Opção invalida, tente novamente')
        resposta = ciclo_nova_operacao()

    elif opcao == 6:
        system('clear')
        opcao = input('''O que deseja EXCLUIR:
    1 - Atividade
    2 - Categoria\n''')
        opcao =  opcao_valida(opcao)
        if opcao == 1:
            excluir_dado('atividade')
        elif opcao == 2:
            excluir_dado('categoria')
        else:
            print('Opção invalida, tente novamente')
        resposta = ciclo_nova_operacao()
    
    else:
        print('Opção invalida, tente novamente')
