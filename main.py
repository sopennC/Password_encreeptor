import os
import display
import generator_v2 as gen


def main():
    try:
        while True:
            display.welcome_message()
            
            choice = input("\nВыберите опцию (1-4): ")
            os.system('cls')
                    
            if choice == "1":
                display.choice1()
                print(display.colorize_terminal("\nВведите логин:  ", display.Color.Green), end='')

                login = input("")

                display.question_about_length()


                
            if choice == '3':
                display.choice3()

    except KeyboardInterrupt:
        display.complete_code()

if __name__ == "__main__":
    main()
1