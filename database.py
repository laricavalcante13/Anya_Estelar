import sqlite3

def get_high_score():
    conn = sqlite3.connect('anya_records.db')
    cursor = conn.cursor()
    # Cria a tabela se ela não existir
    cursor.execute('CREATE TABLE IF NOT EXISTS scores (valor INTEGER)')
    
    # Busca o maior valor
    cursor.execute('SELECT MAX(valor) FROM scores')
    resultado = cursor.fetchone()[0]
    
    conn.close()
    return resultado if resultado is not None else 0

def save_score(novo_score):
    conn = sqlite3.connect('anya_records.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO scores (valor) VALUES (?)', (novo_score,))
    conn.commit()
    conn.close()