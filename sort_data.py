from datetime import datetime

import pandas as pd

from read_file import read_file
def search_in_data():
    df = read_file()
    print(df)
    choice_left = input("Данные выведутся в консоль.\n"
                       "Введите дату в начала периода в формате (yyyy-mm-dd)")
    choice_right = input("Введите дату конца периода в формате (yyyy-mm-dd)")
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    sort_df = df.loc[(df['Date'] >= choice_left)
                         & (df['Date'] < choice_right)]
    print(sort_df)



