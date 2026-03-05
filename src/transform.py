import pandas as pd

def transform_data(df):
    #eliminar duplicados
    df = df.drop_duplicates()

    df = df.fillna(0)

    return df