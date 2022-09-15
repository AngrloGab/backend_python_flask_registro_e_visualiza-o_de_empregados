import sqlite3

#Escolhendo o nome do banco de dados
conn = sqlite3.connect('enterprise.db')
cursor = conn.cursor()

cursor.execute(""" 

        CREATE TABLE empregados (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cargo TEXT,
            salario REAL
        );

""")

print("tabela criada com sucesso")

#Desconectando o banco
conn.close()