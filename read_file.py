import pandas as pd

def read_file(): # чтением
    return pd.read_csv("file_csv.csv", sep=";")