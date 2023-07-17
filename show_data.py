def show_data():
    print("\nПП | ФИО | Телефон")
    with open('file/example.txt', "r", encoding="utf-8") as data:
        print(data.read())
    print("")