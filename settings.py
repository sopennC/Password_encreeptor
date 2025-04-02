import string
import re

# PATTERN = (lambda: "[" + re.escape("".join(set(string.punctuation) - set("!@#$%^&*-_=+"))) + "]")()
PATTERN = "[" + re.escape("".join(set(string.punctuation) - set("!@#$%^&*-_=+"))) + "]"

PASSWORD_LENGTH = 12 # <--- Длина генерации пароля по дефолту