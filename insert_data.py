import sqlite3

empregados = [
    {"nome":"valentina","cargo":"analista","salario":5000},
    {"nome":"Enzo","cargo":"analista","salario":4000},
    {"nome":"Maria","cargo":"desenvolvedor","salario":5000}
]

conn = sqlite3.connect('enterprise.db')
cursor = conn.cursor()

for empregado in empregados:
    cursor.execute("""
            INSERT INTO empregados(nome,cargo,salario)
            VALUES (?,?,?)
    """,(empregado['nome'],empregado['cargo'],empregado['salario']))

print("Dados inseridos com sucesso")

conn.commit()
conn.close()