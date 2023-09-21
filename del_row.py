from read_file import read_file



def del_row(): # удаление
    df = read_file()
    index_choice = int(input("Какой индекс удалить?: "))
    try:
        df.drop([index_choice])
        print("Строка успешно удалена.")
        return df.to_csv("file_csv.csv", sep=";", index=False)
    except:
        print("Вы ввели несуществующий индекс, попробуйте снова: ")
        del_row()
