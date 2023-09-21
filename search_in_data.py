from read_file import read_file
def search_in_data():
    df = read_file()
    print(df)
    choice = int(input("По какому признаку фильтровать:"
                       "1 - по часам."
                       "2 - по месяцу."
                       "3 - по году."
                       ))

    month = int(input("Введите месяц записи"))
    year = int(input("Введите год записи"))
    df[(df['Date'].dt.month == 12) & (df['Date'].dt.year == 2018)]
