import re
import string
from ugly_code import PATTERN

def check(password):
    match = re.search(PATTERN, password)
    if match:
        return "fuck youre password!"
    else:
        return "Youre password is correct"

def check_length(password):
    if len(password)<8:
        print("Твой пароль слишком короткий")
        return False
    elif len(password)<12:
        print("Твой пароль нормальной длины, но лучше сделать его подлиннее")
        return True
    else:
        print("Твой пароль хорош!")
        return True




if __name__ == "__main__":
    print(check("12312312sdfa"))
    check_length("1231231sdfsdf")
