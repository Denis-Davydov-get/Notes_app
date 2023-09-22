from read_file import read_file
def search_in_data():
    df = read_file()
    print(df)
    choice = int(input("По какому признаку фильтровать:"
                       "1 - по дате."
                       "2 - по месяцу."
                       "3 - по годам."
                       "4 - по часам."
                       "5 - по минутам."
                       "6 - по секундам."
                       ))
    if choice == 1:
        day = int(input("Введите дату записи"))
        df.loc[df['Date'].dt.day == day]




    month = int(input("Введите месяц записи"))
    year = int(input("Введите год записи"))
    df[(df['Date'].dt.month == 12) & (df['Date'].dt.year == 2018)]
