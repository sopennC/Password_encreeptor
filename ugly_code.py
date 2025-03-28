import secrets
import string
import re
'''
Импортируем что-то.   >:(
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
def color(text: str, color: str = "reset") -> str:
    colors = {
        "black": "0;30",    # чорный
        "red": "1;31",      # красный
        "green": "1;32",    # зеленый
        "yellow": "1;33",   # желтый
        "blue": "1;34",     # синий
        "magenta": "1;35",  # фиолетовый
        "cyan": "1;36",     # голубой
        "white": "1;37",    # белый
        "reset": "0"        # СБРОС ДО ЗАВОДСКИХ
    }
    code = colors.get(color.lower(), "0")  # по умолчанию сброс
    return f"\033[{code}m{text}\033[0m"