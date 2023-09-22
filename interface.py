import append_file
import del_row
import edit_file
import read_file
import save_file
import sort_data


def init_choice():
    choice = int(input("Что вы хотите сделать?(Введите цифру):\n"
                       "1 - Прочитать заметки.\n"
                       "2 - Добавить заметку\n"
                       "3 - удалить заметку\n"
                       "4 - сохранить в новый файл\n"
                       "5 - фильтровать по дате\n"
                       "6 - редактировать заметку\n"))


    if choice == 1:
        read_file.read_file()
    elif choice == 2:
        append_file.append_file()
    elif choice == 3:
        del_row.del_row()
    elif choice == 4:
        save_file.save_file()
    elif choice == 5:
        sort_data.search_in_data()
    elif choice == 6:
        edit_file.edit_file()
    else:
        print("Вы ввели не верное число")
        # init_choice()
# except:
#     print("Вы ввели что то не так, попробуйте еще.")

