import sqlite3

# Criação do banco de dados e tabela para armazenar os scores
def init_db():
    conn = sqlite3.connect('anya_records.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS scores (valor INTEGER)')
    conn.commit()
    conn.close()

# Função para salvar o score no banco de dados
def save_score(novo_score):
    conn = sqlite3.connect('anya_records.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO scores (valor) VALUES (?)', (novo_score,))
    conn.commit() 
    conn.close()

# Função para recuperar o recorde do banco de dados
def get_high_score():
    conn = sqlite3.connect('anya_records.db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT MAX(valor) FROM scores')
        resultado = cursor.fetchone()[0]
    except:
        resultado = 0
    conn.close()
    return resultado if resultado is not None else 0