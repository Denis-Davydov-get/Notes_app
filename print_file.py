import pandas as pd
def print_file(): # чтение
    df = pd.read_csv("file_csv.csv", sep=";")
    print(df)

