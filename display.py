import os
import time
import string
import re
from enum import Enum
import generator_v2

# PATTERN = (lambda: "[" + re.escape("".join(set(string.punctuation) - set("!@#$%^&*-_=+"))) + "]")()
PATTERN = "[" + re.escape("".join(set(string.punctuation) - set("!@#$%^&*-_=+"))) + "]"

options = [
                    'Генерировать новый пароль',
                    'Проверить надёжность пароля',
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
        os.system('cls')
        print( colorize_terminal("-" * 80, Color.Cyan))
        print("""
              


\t \t    Завершение программы...   айл би бэк
              
              
              
              """)
        print( colorize_terminal("-" * 80, Color.Cyan))
        time.sleep(0.3)
        os.system('cls')

def choice1():
        os.system('cls')
        print( colorize_terminal("-" * 80, Color.Cyan))
        print( colorize_terminal("\t\t\t\tГенерация пароля", Color.Cyan))
        print( colorize_terminal("-" * 80, Color.Cyan))  


def choice3():
        os.system('cls')
        print_title("Кластер паролей", Color.Cyan)
        

def print_title(title:str, color: Color =  Color.Reset) -> None:
        print( colorize_terminal("-" * 80, color))
        print( colorize_terminal(f"\t\t\t\t{title}", color))
        print( colorize_terminal("-" * 80, color))

def colorize_terminal(text: str, color: Color = Color.Reset) -> str:
    return f"\033[{color.value}m{text}\033[0m"

def question_about_length():
    print(colorize_terminal("\nДлина пароля: 12 символов \nХотите изменить длину пароля? \n 1) Да\n 2) Нет\n", Color.Black),end="")

    answer = input("")
    if answer == '1':
        length = int(input("Введите длину пароля: "))
        generator_v2.generate_password(length)
    elif answer == '2':
        generator_v2.generate_password()
    else:
        os.system("cls")
        print(colorize_terminal("\n\tВведи 1 или 2, лол!", Color.Red))
        question_about_length()