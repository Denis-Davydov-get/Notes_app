from read_file import read_file
def edit_file(): # редактирование
    df = read_file()
    choice_row = int(input("Какую строку вы хотите изменить?: "))
    if 0 <= choice_row <= len(df):
        for i in df.index:
            if i == choice_row:
                choice_edit = int(input("Что вы хотите изменить?:\n"
                                        "1 - заголовок.\n"
                                        "2 - текст.\n"))
                if choice_edit == 1:
                    edit_header = input("Чем заменить заголовок?: ")
                    df.at[choice_row, 'Header'] = edit_header
                    return df.to_csv("file_csv.csv", sep=";", index=False)
                elif choice_edit == 2:
                    edit_text = input("Чем заменить текст?: ")
                    df.at[choice_row, 'Text'] = edit_text
                    return df.to_csv("file_csv.csv", sep=";", index=False)
                else:
                    print("Что-то пошло не так. Попробуйте еще раз.")
                    edit_file()
