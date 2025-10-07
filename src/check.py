from re import *


def check_function(s: str) -> bool:
    """Функция проверки корректности выражения."""
    if '0' not in s and '1' not in s and '2' not in s and '3' not in s and '4' not in s and '5' not in s and '6' not in s and '7' not in s and '8' not in s and '9' not in s:  # есть ли числа в строке
        raise ValueError("Некорректно введено выражение")
    pattern = r'[0-9.][ ][0-9.]'
    z = findall(pattern, s)
    if len(z) > 0 or '  ' in s:  # не может быть пробела между цифрами и не может быть больше 1 пробела
        raise ValueError("Некорректно введено выражение")
    s = s.replace(' ', '')  # убираем пробелы
    i = 0  # индекс строки
    state = "Первый символ"  # состояние (какой был символ до)
    balance = 0  # подсчет скобок
    while i < len(s):  # проверка порядка символов
        if s[-1] not in '1234567890)':  # проверка последнего символа отдельно
            raise ValueError("Некорректно введено выражение")
        if s[i] in '1234567890':
            if state != "Закрывающаяся скобка":
                state = "Цифра"
                i += 1
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in '.':
            if state == "Цифра":
                i += 1
                state = "Точка"
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in '+-':
            if state == "Первый символ" or state == "Цифра" or state == "Открывающаяся скобка" or state == "Закрывающаяся скобка":
                i += 1
                state = "+ или -"
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in '(':
            balance += 1
            if state != "Цифра" and state != "Точка" and state != "Закрывающаяся скобка":
                i += 1
                state = "Открывающаяся скобка"
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in ')':
            balance -= 1
            if state == "Цифра" or state == "Закрывающаяся скобка":
                i += 1
                state = "Закрывающаяся скобка"
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in '*/':
            if state == "Цифра" or state == "Закрывающаяся скобка":
                i += 1
                state = "* или /"
            elif state == "* или /":
                i += 1
                state = "** или //"
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in '%':
            if state == "Цифра" or state == "Закрывающаяся скобка":
                i += 1
                state = "%"
            else:
                raise ValueError("Некорректно введено выражение")
        else:
            raise ValueError(f"Введен неверный символ: {s[i]}")
        if balance >= 0:
            pass
        else:
            raise ValueError("Некорректно введено выражение")
    if balance == 0:  # все скобки закрыты
        pass
    else:
        raise ValueError("Некорректно введено выражение9")
    return True
