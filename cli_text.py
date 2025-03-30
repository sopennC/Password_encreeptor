import os
import time
import ugly_code as ugly
from ugly_code import Color

options = [
                    'Генерировать новый пароль',
                    'Проверить надёжность пароля',
                    'Открыть кластер паролей',
                    'Выйти'
        ]

def welcome():
    print("=" * 40)
    print(ugly.colorize_terminal('\t    Менеджер паролей', ugly.Color.Cyan))
    print("=" * 40)
    print(f"\n{ugly.colorize_terminal('Возможности:', ugly.Color.Yellow)}\n")
    for index, value in enumerate(options, start=1):
                        print(ugly.colorize_terminal(str(index) + ")", ugly.Color.Green), end=" ")
                        print(value)

def go_out():
        os.system('cls')
        print(ugly.colorize_terminal("-" * 80, ugly.Color.Cyan))
        print("""
              


\t \t    Завершение программы...   айл би бэк
              
              
              
              """)
        print(ugly.colorize_terminal("-" * 80, ugly.Color.Cyan))
        time.sleep(1.3)
        os.system('cls')

def choice1():
        os.system('cls')
        print(ugly.colorize_terminal("-" * 80, ugly.Color.Cyan))        # 
        print(ugly.colorize_terminal("\t\t\t\tГенерация пароля", ugly.Color.Cyan))
        print(ugly.colorize_terminal("-" * 80, ugly.Color.Cyan))  
        
        print(ugly.colorize_terminal("\nВведите логин:  ", ugly.Color.Green), end='')
        login = input("")


def choice3():
        os.system('cls')
        print_title("Кластер паролей",Color.Cyan)
        

def print_title(title:str, color:ugly.Color = ugly.Color.Reset) -> None:
        print(ugly.colorize_terminal("-" * 80, color))
        print(ugly.colorize_terminal(f"\t\t\t\t{title}", color))
        print(ugly.colorize_terminal("-" * 80, color))

def ABCD():
        digit = input()
        if int(digit) in range(len(options)+1):
                print ("ok")