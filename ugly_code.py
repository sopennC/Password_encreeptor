import secrets
import string
import re
from enum import Enum

'''

>:(

'''





'''
Создание PATTERN для не нужных символов в пароле
'''

allpunctuation = set(string.punctuation) # Вся существующая пунктуация
nicepunctuation = set("!@#$%^&*-_=+") # Прикольная допустимая пунктуация
wrong_expectation = str(allpunctuation.symmetric_difference(nicepunctuation))  # вычитаем из ВСЕЙ - прикольную, и получаем то что нам нельзя использовать в паролях
PATTERN = "[" + re.escape("".join(wrong_expectation)) + "]"  # Страшно выглядящая строчка с экранизацией всех "плохих" символов


'''
Расскраска нашего str для вывода в терминальчик
просто пишем :   print(ugly.color("Наше сообщение","цвет"))
'''
class Color(Enum):
        Black = "0;30"    # чорный
        Red = "1;31"      # красный
        Green = "1;32"    # зеленый
        Yellow = "1;33"   # желтый
        Blue = "1;34"     # синий
        Magenta = "1;35"  # фиолетовый
        Cyan = "1;36"     # голубой
        White = "1;37"    # белый
        Reset = "0"       # СБРОС ДО ЗАВОДСКИХ

def colorize_terminal(text: str, color: Color = Color.Reset) -> str:
    return f"\033[{color.value}m{text}\033[0m"