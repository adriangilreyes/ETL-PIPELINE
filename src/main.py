from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    #extract
    df = extract_data()
    print('Datos extraidos')

    #transform
    df_clean = transform_data(df)
    print('Datos transformados')

    #load
    load_data(df_clean)
    print('Datos cargados en la base de datos')

if __name__ == "__main__":
    main()