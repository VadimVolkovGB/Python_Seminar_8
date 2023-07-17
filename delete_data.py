def delete_data():
    print("\nПП | ФИО | Телефон")
    with open('file/example.txt', "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))