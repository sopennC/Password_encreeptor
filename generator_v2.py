import secrets
import string
import re
from evaluator import PATTERN


PASSWORD_LENGTH = 12 # <--- Длина пароля


def generate_prep(length=PASSWORD_LENGTH, use_digits=True, use_special=True) -> str:

    chars = string.ascii_letters

    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*-_=+"
    
    return "".join(secrets.choice(chars) for _ in range(length))

def generate_password(length=PASSWORD_LENGTH, use_digits=True, use_special=True):
    while True:
        prep = generate_prep(length, use_digits, use_special)
        if (
            has_digits(prep)
            and has_lowercase(prep)
            and has_uppercase(prep)
            and not check_pattern(prep)
        ):
            return prep

def has_digits(p) -> bool: return bool(re.search(r'\d',p))           # Проверка на содержание 123           -> True если нашел
def has_lowercase(p) -> bool: return bool(re.search(r'[a-z]',p))     # Проверка на содержание str           -> True если нашел
def has_uppercase(p) -> bool: return bool(re.search(r'[A-Z]',p))     # Проверка на содержание STR           -> True если нашел
def check_pattern(p) -> bool: return bool(re.search(PATTERN,p))      # Проверка на содержание ;'.,""{}[]    -> True если нашел
   

if __name__ == "__main__":
    pswrd = generate_password(20,True,True)  # Просто проверка
    print(pswrd)