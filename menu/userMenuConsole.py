import sys
sys.path.append('Users\Mikhail\Desktop\GeekBrains\Проект')
import menuTemplates


def menu_console():
        menuTemplates.printNenuTitle("Главное меню\n           Журнал заметок")
        print("1 - вывод журнала \n2 - вывод заметки по id \n3 - выбор заметки по дате\n4 - редактирование заметки"
              " \n5 - добавление заметки\n6 - удаление заметки\n7 - выход")
        menuTemplates.printMenuLine()
        print("\n введите пункт из меню ")

