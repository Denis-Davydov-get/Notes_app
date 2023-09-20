import time
import numpy as np
import pandas as pd
def read_file(): # чтением
    return pd.read_csv("file_csv.csv", sep=";")
def append_file(): # добавление
    header = input("Введите заголовок:")
    text = input("Введите текст:")
    file = read_file()
    new_df = pd.DataFrame({"id":[len(read_file().index)],
                           "Header":[header],
                           "Text":[text],
                           "Time":[time.ctime()]},
                          )
    result = file._append(new_df, ignore_index = True )
    return result.to_csv("file_csv.csv", sep=";", index=False)
def save_file(): # сохранение
    name_file = input("Как назвать файл?: ")
    return read_file().to_csv(name_file + ".csv", sep=";")
def edit_file(data): # редактирование
    pass
def del_row(): # удаление
    index = int(input("Какой индекс удалить?: "))
    df = read_file()
    index_file = len(read_file().index)
    if index_file < index | index_file > index:
        print("Вы ввели несуществующий индекс, попробуйте снова: ")
        del_row()
    else:
        df.drop(labels=[index], axis=0, inplace=True)
        print("Строка" + index + "успешно удалена.")
        return df.to_csv("file_csv.csv", sep=";", index=False)





del_row()