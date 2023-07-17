from user import choose_mode
from filling_phone_books import filling
from delete_data import delete_data
from show_data import show_data
from edit_data import edit_data
from export_data import export_data

def running():
    person, mode = choose_mode()
    if mode == 'запись':
        filling(person)
    else:
        pass
    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 - Вывести инфо на экран")
        print("2 - Произвести экпорт данных")
        print("3 - Произвести изменение данных")
        print("4 - Произвести удаление данных")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            export_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        else:
            my_choice = 0
