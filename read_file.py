import pandas as pd
def read_file(): # чтение
    df = pd.read_csv("file_csv.csv", sep=";")
    return df

