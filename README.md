## Descrição
    O projeto consiste em um aplicativo em CLI (Interface de Linha de Comando) escrito 
    em Python, que se conecta ao banco de dados MySQL para organizar tarefas. O objetivo 
    do aplicativo é permitir que o usuário organize suas tarefas em categorias específicas 
    e acompanhe seu progresso através do status de execução e da data de conclusão.

    O aplicativo é composto por três módulos principais: o módulo de criação e conexão 
    com o banco de dados MySQL, o módulo de funções de consulta e o módulo principal de 
    chamadas para as funções. O módulo de criação e conexão com o banco de dados é responsável 
    por criar a conexão com o banco de dados MySQL e configurar a tabela para armazenar as 
    informações das tarefas. O módulo de funções de consulta contém as funções que permitem 
    que o usuário crie, atualize e consulte as tarefas, categorias, status de execução e datas 
    de conclusão. O módulo principal é responsável por chamar as funções de consulta e interagir 
    com o usuário por meio de uma interface de linha de comando.

    Ao iniciar o aplicativo, o usuário será apresentado a um menu de opções que inclui a criação 
    de uma nova tarefa, a atualização de uma tarefa existente, a exclusão de uma tarefa e a 
    consulta de tarefas existentes, categorias e datas de conclusão. Para criar uma nova tarefa, 
    o usuário deve fornecer um título, uma descrição, uma categoria e uma data de conclusão. 
    O usuário também pode definir o status da tarefa como "pendente", "em andamento" ou "concluída". 
    As tarefas criadas são armazenadas no banco de dados e podem ser consultadas a qualquer momento 
    por meio das opções de consulta.

    As opções de consulta permitem que o usuário filtre as tarefas por categoria e data de conclusão. 
    O usuário pode visualizar uma lista de tarefas que correspondam aos seus critérios de filtragem 
    e verificar seu status de execução atual. Além disso, o usuário pode atualizar o status de 
    execução e a data de conclusão de uma tarefa existente ou excluir uma tarefa que já foi concluída.

    Em resumo, o aplicativo em CLI escrito em Python com o banco de dados MySQL para organização de 
    tarefas separadas por categorias, que incluem data e status de execução, é uma solução simples e 
    eficaz para gerenciar e acompanhar tarefas pessoais ou profissionais. Ele oferece ao usuário uma 
    maneira fácil de criar, atualizar e consultar tarefas, além de permitir que ele personalize suas 
    categorias e filtre as tarefas por datas de conclusão. O projeto é uma ótima opção para quem 
    busca uma solução de gerenciamento de tarefas personalizada e flexível, sem precisar recorrer a 
    ferramentas mais complexas e com recursos desnecessários.

## Status do Projeto
    Este projeto ainda está em andamento e em fase de desenvolvimento ativo. As funcionalidades 
    descritas neste documento estão sujeitas a mudanças e adições. A documentação será atualizada 
    à medida que novas funcionalidades forem adicionadas.

    É importante incluir essa informação na documentação para deixar claro para os usuários e 
    colaboradores que o projeto não está finalizado e que ainda pode passar por mudanças significativas. 
    Isso evita possíveis confusões ou expectativas equivocadas por parte dos usuários.

## Instalação
    Para executar este código, você precisará instalar o pacote mysql-connector-python usando o pip. 
    Você pode fazer isso executando o seguinte comando:
    -pip install mysql-connector-python

## Uso
    Para usar este código, siga os seguintes passos:

    1. Edite o arquivo database_mysql.py e ajuste os valores de host, user, password e database de acordo com o seu ambiente.
    2. Edite o arquivo queries.py e ajuste as consultas SQL de acordo com a estrutura da sua tabela.
    3. Execute o arquivo main.py para fazer chamadas às funções de consulta.

## Contribuição
    Se você quiser contribuir para este projeto, siga os seguintes passos:
    
    Faça um fork deste repositório.
    Crie uma nova branch para suas alterações.
    Faça as alterações desejadas e teste-as.
    Envie uma pull request para que suas alterações sejam revisadas e mescladas.