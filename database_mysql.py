import mysql.connector
import passsword

def abrir_conexao():
    conexao = mysql.connector.connect(

            host = "localhost",
            user = "root",
            password = passsword.senha,
            database = "gerenciamento_de_tarefas",
            auth_plugin = 'mysql_native_password'
        )
    
    return conexao

def criando_database():
    try:    
        conexao = abrir_conexao()
    except:
        conexao = mysql.connector.connect(

            host = "localhost",
            user = "root",
            password = passsword.senha,
            auth_plugin = 'mysql_native_password'
        )
        cursor = conexao.cursor()
        cursor.execute('CREATE DATABASE if not exists gerenciamento_de_tarefas')

        conexao = abrir_conexao()
        cursor = conexao.cursor()

        cursor.execute('''CREATE TABLE if not exists categoria (
        	id INT UNSIGNED auto_increment NOT NULL,
        	categoria varchar(100) NOT NULL,
        	CONSTRAINT categoria_PK PRIMARY KEY (id),
        	CONSTRAINT categoria_UN UNIQUE KEY (categoria)
        )
        ENGINE=InnoDB
        DEFAULT CHARSET=utf8mb4
        COLLATE=utf8mb4_0900_ai_ci;''')
        conexao.commit()

        cursor.execute('''CREATE TABLE if not exists atividade (
            id int NOT NULL AUTO_INCREMENT,
            nome varchar(100) NOT NULL,
            data date NOT NULL,
            categoria int unsigned NOT NULL,
            status enum('nao','sim') NOT NULL DEFAULT 'nao',
            PRIMARY KEY (id),
            UNIQUE KEY nameUN (nome),
            KEY atividade_FK (categoria),
            CONSTRAINT atividade_FK FOREIGN KEY (categoria) REFERENCES categoria (id) ON DELETE CASCADE ON UPDATE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')
        conexao.commit()
    return conexao
