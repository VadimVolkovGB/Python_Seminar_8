def export_data():
    with open('file/example.txt', "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open('file/example.txt', "a", encoding="utf-8") as data:
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        data.write(f"{num} | {fio} | {phone_number}\n")
        print(f"Добавлена запись : {num} | {fio} | {phone_number}\n")