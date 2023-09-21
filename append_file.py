import time
import pandas as pd
import read_file


def append_file(): # добавление
    header = input("Введите заголовок:")
    text = input("Введите текст:")
    df = read_file.read_file()
    append_df = pd.DataFrame(dict(id=[len(df)],
                                  Header=[header],
                                  Text=[text],
                                  Date=[time.strftime('%d:%m:%Y')],
                                  Time=[time.strftime('%H:%M:%S')])
                             )

    result = df._append(append_df, ignore_index = True)
    return result.to_csv("file_csv.csv", sep=";", index=False)
