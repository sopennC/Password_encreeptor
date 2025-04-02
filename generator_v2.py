import secrets
import string
import re
from settings import PATTERN, PASSWORD_LENGTH

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
            and check_pattern(prep) 
            and not check_badpattern(prep) 
        ):
            return prep
        else:
            generate_password(length, use_digits, use_special)
def has_digits(p) -> bool: return bool(re.search(r'\d',p))
def has_lowercase(p) -> bool: return bool(re.search(r'[a-z]',p))
def has_uppercase(p) -> bool: return bool(re.search(r'[A-Z]',p))
def check_badpattern(p) -> bool: return bool(re.search(PATTERN,p))
def check_pattern(p) -> bool: return bool(re.search(r"[!@#$%^&*-_=+]",p))

print(generate_password())