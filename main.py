import os
import display
import generator_v2 as gen
import crypto


def main():
    try:
        while True:
            display.welcome_message()
            
            choice = input("\nВыберите опцию (1-4): ")
            os.system('cls')
                    
            if choice == "1":
                display.choice1()
                login = input("\nВведите название для пароля:  " end='')
                display.question_about_length()



                
            if choice == '3':
                display.choice3()

    except KeyboardInterrupt:
        display.complete_code()

if __name__ == "__main__":
    main()