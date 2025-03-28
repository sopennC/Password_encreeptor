import os
import time
import ugly_code as ugly

options = [
                    'Генерировать новый пароль',
                    'Проверить надёжность пароля',
                    'Открыть кластер паролей',
                    'Выйти'
        ]

def welcome():
    print("=" * 40)
    print(ugly.color('\t    Менеджер паролей',"cyan"))
    print("=" * 40)
    print(f"\n{ugly.color('Возможности:',"yellow")}\n")
    for index, value in enumerate(options, start=1):
                        print(ugly.color(str(index) + ")", "green"), end=" ")
                        print(value)

def go_out():
        os.system('cls')
        print(ugly.color("-" * 80, "cyan"))
        print("""
              


\t \t    Завершение программы...   айл би бэк
              
              
              
              """)
        print(ugly.color("-" * 80, "cyan"))
        time.sleep(1.3)
        os.system('cls')