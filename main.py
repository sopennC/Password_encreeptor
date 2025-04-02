import os
import display
import crypto
import time

def main():
    try:
        while True:
            os.system("cls")
            display.welcome_message()
            
            choice = input("\nВыберите опцию (1-4): ")
            os.system('cls')
                    
            if choice == "1":
                display.choice1()
                name = input("\nВведите название сервиса:  ")
                login = input("\nВведите логин:  ")
                password = display.question_about_length()
                display.confirmation(login, name, password)

            if choice == '2':
                display.choice2()
                name = input("\nВведите название сервиса:  ")
                login = input("\nВведите логин:  ")
                password = input("\nВведите пароль:  ")
                os.system("cls")
                display.confirmation(login, name, password)

                
            if choice == '3':
                display.choice3()

                names = crypto.list_names()
                if not names:
                    print(display.colorize_terminal("\nПока тут ничего нет ...  \n", display.Color.Blue))
                    input("Нажмите 'Enter' чтобы вернуться: ")
                    os.system("cls")
                else:
                    print("Список доступных записей:")
                    for i, name in enumerate(names, start=1):
                        print(f"{i}. {name}")

                    try:
                        index = int(input("\nВыберите номер записи: ")) - 1
                        if 0 <= index < len(names):
                            selected_name = names[index]
                            crypto.get_entry(selected_name)
                            input("\nНажмите 'Enter' чтобы вернуться: ")
                        else:
                            print("Неверный номер.")
                    except ValueError:
                        print("Введите корректный номер.")

            if choice == '4':
                print(display.colorize_terminal("\nНадеюсь еще увидимся ...  \n", display.Color.Magenta))
                time.sleep(0.5)
                exit()


    except KeyboardInterrupt:
        display.complete_code()

if __name__ == "__main__":
    main()