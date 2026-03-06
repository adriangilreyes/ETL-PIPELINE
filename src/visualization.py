import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#conexión a la base de datos
conn = sqlite3.connect('database/etl.db')

#leemos los datos
df = pd.read_sql_query('SELECT * FROM spambase',conn)

#cerramos la conexión
conn.close()

#gráfico
plt.title('Spam vs No Spam')
df['class'].value_counts().plot(kind='bar')
plt.show()

plt.title('Gráfico de frecuencias columnas numéricas DF') 
df['capital_run_length_total'].hist()
plt.show()
