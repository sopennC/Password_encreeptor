import os
import time
from enum import Enum
import generator_v2
import crypto


options = [
                    'Генерировать новый пароль',
                    'Ввести свой пароль',
                    'Открыть кластер паролей',
                    'Выйти'
        ]

class Color(Enum):
        Black = "0;30"    # чорный
        Red = "1;31"      # красный
        Green = "1;32"    # зеленый
        Yellow = "1;33"   # желтый
        Blue = "1;34"     # синий
        Magenta = "1;35"  # фиолетовый
        Cyan = "1;36"     # голубой
        White = "1;37"    # белый
        Reset = "0"       # СБРОС ДО ЗАВОДСКИХ

def welcome_message():
    print("=" * 40)
    print( colorize_terminal('\t    Менеджер паролей', Color.Cyan))
    print("=" * 40)
    print(f"\n{ colorize_terminal('Возможности:', Color.Yellow)}\n")
    for index, value in enumerate(options, start=1):
                        print( colorize_terminal(str(index) + ")", Color.Green), end=" ")
                        print(value)

def complete_code():
        os.system('clear')
        print( colorize_terminal("-" * 80, Color.Cyan))
        print("""
              


\t \t    Завершение программы...   айл би бэк
              
              
              
              """)
        print( colorize_terminal("-" * 80, Color.Cyan))
        time.sleep(0.3)
        os.system('clear')

def choice1():
        os.system('clear')
        print( colorize_terminal("-" * 80, Color.Cyan))
        print( colorize_terminal("\t\t\t\tГенерация пароля", Color.Cyan))
        print( colorize_terminal("-" * 80, Color.Cyan))  

def choice2():
        os.system('clear')
        print( colorize_terminal("-" * 80, Color.Cyan))
        print( colorize_terminal("\t\t\t\tСвой пароль", Color.Cyan))
        print( colorize_terminal("-" * 80, Color.Cyan))  

def choice3():
        os.system('clear')
        print_title("Кластер паролей", Color.Cyan)
        

def print_title(title:str, color: Color =  Color.Reset) -> None:
        print( colorize_terminal("-" * 80, color))
        print( colorize_terminal(f"\t\t\t\t{title}", color))
        print( colorize_terminal("-" * 80, color))

def colorize_terminal(text: str, color: Color = Color.Reset) -> str:
    return f"\033[{color.value}m{text}\033[0m"

def question_about_length():
    print(colorize_terminal("\nДлина пароля: 12 символов \nХотите изменить длину пароля? \n\n 1) Да\n 2) Нет\n\n", Color.Black),end="")

    answer = input("Что ответите? : ")
    if answer == '1':
        try:
                length = int(input("\nВведите длину пароля: "))
                if length < 8:
                       print(colorize_terminal("\nДлина пароля должна быть больше 8! ", Color.Red))
                       input("\nНажмите 'Enter' чтобы вернуться: ")
                       os.system("clear")
                       return question_about_length()
                else:
                        password = generator_v2.generate_password(length)
                        os.system('clear')
                        return password
        except ValueError:
               print("\nВведите цифру! ")
               input("\nНажмите 'Enter' чтобы вернуться: ")
               return question_about_length()

    elif answer == '2':
        password = generator_v2.generate_password()
        os.system("clear")
        return password
    else:
        os.system("clear")
        print(colorize_terminal("\n\tВведи 1 или 2, лол!", Color.Red))
        return question_about_length()

def confirmation(login, name , password):
        print(colorize_terminal("Проверьте данные\nТут можете скопировать пароль :)  \n",Color.Red))
        print(f'Имя для поиска пароля в кластере =   {name}')
        print(f'Ваш логин =   {login}')
        print(f'Ваш пароль =   {password}')

        print(colorize_terminal("\nВсе хорошо? \n\n 1) Да\n 2) Нет\n\n", Color.Black),end="")
        answer = input("")
        if answer == '1':
                crypto.save_generated(name, login, password)
                print(colorize_terminal("\nПароль успешно сохранен в кластер!\n", Color.Red))
                input("Нажмите 'Enter' чтобы вернуться: ")
        elif answer == '2':
                os.system("clear")
                print(colorize_terminal("\nПрервано :(\n", Color.Red))
                input("Нажмите 'Enter' чтобы вернуться: ")
        else:
                confirmation(login, name , password)