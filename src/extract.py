import pandas as pd


def extract_data():
    df = pd.read_csv('C:/Users/Usuario/Desktop/ProyectosPython/etl_project/data/raw/spambase_csv.csv')
    return df

print(extract_data())


 