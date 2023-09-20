from datetime import *
import pandas as pd
import read_file
def append_file(): # добавление
    header = input("Введите заголовок:")
    text = input("Введите текст:")
    file = read_file.read_file()
    new_df = pd.DataFrame({"id":[len(read_file.read_file().index)],
                           "Header":[header],
                           "Text":[text],
                           "Date":[datetime.now().strftime("%H:%M:%S")]},
                          )
    result = file._append(new_df, ignore_index = True)
    return result.to_csv("file_csv.csv", sep=";", index=False)