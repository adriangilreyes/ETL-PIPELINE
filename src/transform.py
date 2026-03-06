import pandas as pd

def transform_data(df):
    #eliminar duplicados
    df = df.drop_duplicates()

    df = df.fillna(0)

    df.to_csv('data/processed/spambase_clean.csv',index=False)

    return df

