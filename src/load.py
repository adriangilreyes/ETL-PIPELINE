import sqlite3

def load_data(df):
    conn = sqlite3.connect('database/etl.db')

    #cargamos la tabla
    df.to_sql('spambase',conn, if_exists='replace', index=False)

    conn.close()