from database_mysql import criando_database, abrir_conexao
from os import system  


#LEMBRAR DE TIRAR O ARQUIVO DE PASSWORDS

conexao = criando_database()
print(conexao)
cursor = conexao.cursor()

def pesquisa_dados(nome_tabela, where_like , parametro, id):
    if nome_tabela == 'categoria':
        if parametro != None:
            cursor.execute(f'SELECT id, categoria from categoria WHERE categoria like "%{parametro}%";') 
            print(f'    {"|"}{"Nome":_^25}')
        else:
            cursor.execute(f'SELECT id, categoria from categoria ;') 
            print(f'    {"|"}{"Nome":_^25}')
    else:
        if where_like == None:
            cursor.execute(f'SELECT a.id, a.nome, c.categoria, status, data  from atividade a join categoria c on a.categoria = c.id;')
        elif where_like == 'categoria':
            cursor.execute(f'SELECT a.id, a.nome, c.categoria, status, data  from atividade a join categoria c on a.categoria = c.id WHERE c.{where_like} like "%{parametro}%";')
        else:    
            cursor.execute(f'SELECT a.id, a.nome, c.categoria, status, data  from atividade a join categoria c on a.categoria = c.id WHERE a.{where_like} like "%{parametro}%";')
        print(f'    |{"Nome":_^25}|{"Categoria":_^25}|{"Status":_^25}|{"Data":_^25}|')  
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print(f'Não existe nenhuma {nome_tabela} cadastrada')
        opcao = input('Deseja cadastrar [S/N]: ').strip().upper()[0]
        if opcao == 'S':
            novo_cadastro(f'{nome_tabela}')
    c = 0
    dado_temporario = []
    dado = []
    dado_final = []
    while c < len(resultado):
        i = 0
        print(f'\n{c+1}°',end='- |')
        while i < len(resultado[c]):
            dado_temporario.append(resultado[c][i])
            dado.append(dado_temporario[:])
            if i > 0 and i < len(resultado[c]):
                valor = str(resultado[c][i])
                print(f'{valor:^25}',end='|')
                dado_temporario.clear()
            i+=1
        dado_final.append(dado[:])
        dado.clear()
        c += 1
        print()
    if id == 'return':
        id = return_id(resultado)
        return id

def return_id(resultado):
    c = 0
    dado_temporario = []
    dado = []
    dado_final = []
    while c < len(resultado):
        i = 0
        while i < len(resultado[c]):
            dado_temporario.append(resultado[c][i])
            dado.append(dado_temporario[:])
            dado_temporario.clear()
            i+=1
        dado_final.append(dado[:])
        dado.clear()
        c += 1  
    atividade = int(input('\nSelecione a opção que deseja: ')) 
    dado.append(dado_final[atividade-1])
    id = dado[0][0]
    id = id[0]
    return id

def ano_mes_dia(data):
    while True:
        teste_data = ''
        for i in data:
            if i.isdigit() == True:
                teste_data += i
        if len(teste_data) < 8:
            data = input('A data deve conter 8 numeros\nDigite a data: ')
        else:
            break
    converter_data = ''
    for i in teste_data:
        converter_data += i
        if len(converter_data) == 2:
            converter_data = converter_data + ','
        elif len(converter_data) == 5:
            converter_data = converter_data + ','
    converter_data = converter_data.split(',')
    converter_data.insert(0,converter_data[2])
    converter_data.insert(3,converter_data[1])
    converter_data.pop(4)
    converter_data.pop(1)
    data = ''
    for i in converter_data:
        data = data +i  
    return data

def novo_cadastro(nome_tabela):

    while True:
        system('clear')
        if nome_tabela == 'categoria':
            nova_categoria = str(input('Qual categoria será cadastrada?\n')).capitalize()
            cursor.execute(f'insert into categoria (categoria) values ("{nova_categoria}");')
            print('\nCategoria adicionada\n')
        else:
            nova_atividade = str(input('Qual atividade será programada?\n')).capitalize()
            print('\nQual a categoria dessa atividade?')
            id_categoria = pesquisa_dados('categoria', None, None, 'return')
            data = ''
            data = str(input('\nQual a data de execução dessa atividade?\n'))
            data = ano_mes_dia(data)
            cursor.execute(f'insert into atividade (nome, data, categoria) values ("{nova_atividade}", "{data}", {id_categoria});')
            print('\nAtividade adicionada\n')
        
        conexao.commit()
        resposta = ''
        while resposta != 'N' and resposta != 'S':
            resposta = input(f'Adicionar outra {nome_tabela} [S/N]?  ').strip().upper()[0]
        if resposta == 'N':
            break

def status():
    while True:
        system('clear')
        atividade = input('Qual atividade já foi executada?\n').capitalize()
        id = pesquisa_dados('atividade', 'nome', atividade, 'return')
        cursor.execute(f'update atividade set status = "Sim" WHERE id = {id};')
        conexao.commit()
        print('Status atualizado')
        resposta = ''
        while resposta != 'N' and resposta != 'S':
            resposta = input('Atualizar status de outra atividade[S/N]: ').strip().upper()[0]
        if resposta == 'N':
            break

def excluir_dado(nome_tabela):
    while True:
        system('clear')
        if nome_tabela == 'categoria':
            categoria = str(input('Qual categoria deseja EXCLUIR\n' ))
            id = pesquisa_dados('categoria', categoria)
            print(id)
            cursor.execute(f'''DELETE FROM categoria WHERE id = {id};''')
            print('Categoria excluida')
        else:
            opcao = int(input('''
            1° - Excluir todas as atividades concluidas
            2° - Excluir atividade especifica\n
            Selecione uma opção:'''))

            if opcao == 1:
                cursor.execute('''DELETE FROM atividade WHERE status = "sim";''')

            elif opcao == 2:
                atividade = input('Qual atividade sera excluida?\n').capitalize()
                id = pesquisa_dados(atividade)
                cursor.execute(f'''DELETE FROM atividade WHERE id = {id};''')
            print('Atividades excluidas')
        conexao.commit()
        resposta = ''
        while resposta != 'N' and resposta != 'S':
            resposta = input('Efetuar outra exclusão[S/N]:  ').strip().upper()[0]
        if resposta == 'N':
            break

def atualizar_dados(nome_tabela):
    while True:
        system('clear')
        if nome_tabela == 'categoria':
            categoria = str(input('Qual categoria sera atualizada? ').strip().capitalize())
            id  = pesquisa_dados(nome_tabela, 'nome', categoria, 'return')
            atualizacao = str(input('Digite o dado atualizado?\n')).strip().capitalize()
            cursor.execute(f'UPDATE {nome_tabela} SET categoria = "{atualizacao}"  WHERE id = {id};')  
            
        else:
            atividade = str(input('Qual atividade será atualizada?\n'))
            id_pk = pesquisa_dados(nome_tabela, 'nome', atividade, 'return')
            coluna = str(input('Qual campo atualizar?\n')).strip().lower()
            if coluna == 'categoria':
                id_fk = pesquisa_dados('categoria', None, None, 'return')
                cursor.execute(f'UPDATE atividade SET {coluna} = {id_fk}  WHERE id = {id_pk};')
            else:
                atualizacao = str(input('Digite o dado atualizado?\n')).strip().capitalize()
                if coluna == 'data':
                    atualizacao = ano_mes_dia(atualizacao)
                cursor.execute(f'UPDATE atividade SET {coluna} = "{atualizacao}"  WHERE id = {id_pk};')
            print(f'Os dados da coluna {coluna} foram atualizados')
        conexao.commit()
        resposta = ''
        while resposta != 'N' and resposta != 'S':
            resposta = input(f'Atualizar outra {nome_tabela}[S/N]?  ').strip().upper()[0]
        if resposta == 'N':
            break

def ciclo_nova_operacao(resposta=''):
    while resposta != 'N' and resposta != 'S':
        resposta = str(input('\nDeseja realizar outra operação?--> ')).strip().upper()[0]
    if resposta == 'N':
        print('Programa encerrado')
    system('clear')
    return resposta

def opcao_valida(opcao):
    while True:
        try:
            opcao = int(opcao)
            print(opcao)
            break
        except ValueError:
            opcao = input('Por favor digite o numero da opção')
    return opcao