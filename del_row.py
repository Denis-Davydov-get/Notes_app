from datetime import *
from read_file import read_file



def del_row(): # удаление
    index = int(input("Какой индекс удалить?: "))
    df = read_file()
    index_file = len(read_file().index)
    if 0 < index < index_file:
        print("Вы ввели несуществующий индекс, попробуйте снова: ")
        del_row()
    else:
        df.drop([index])
        print("Строка успешно удалена.")
        return df.to_csv("file_csv.csv", sep=";", index=False)