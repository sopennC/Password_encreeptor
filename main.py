import os
import cli_text as cli
import ugly_code as ugly
import generator_v2 as gen

def main():
    try:
        while True:
            cli.welcome()
            
            choice = input("\nВыберите опцию (1-4): ")
            os.system('cls')
                    
            if choice == "1":
                cli.choice1()
                print(ugly.colorize_terminal("\nВведите длину пароля: ", ugly.Color.Black),end="")
                try:
                    digit = input()
                    # int(digit) <= len(options) and int(digit) >= 0 НАПИСАТЬ ФУНКЦИЮ ЗАВтра бич!
                except ValueError as e:
                    print(f"change value Error: {e}")
                
                    ugly.colorize_terminal("\nВведете нормально цифру")
                    _ = input()
                gen.generate_password()
                print(ugly.colorize_terminal("\nВаш пароль: "))
                
            if choice == '3':
                cli.choice3()

                
            
        
    except KeyboardInterrupt:
        cli.go_out()
        






if __name__ == "__main__":
    main()