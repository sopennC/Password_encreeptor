import os
import cli_text as cli

def main():
    try:
        while True:
            cli.welcome()
            
            choice = input("\nВыберите опцию (1-4): ")
            os.system('cls')
                    
            if choice == "1":
                print("Напишите Логин ...")
        
    except KeyboardInterrupt:
        cli.go_out()
        






if __name__ == "__main__":
    main()