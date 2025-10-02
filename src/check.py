from re import *


def check_function(s):
    """Функция проверки корректности выражения."""
    if '0' not in s and '1' not in s and '2' not in s and '3' not in s and '4' not in s and '5' not in s and '6' not in s and '7' not in s and '8' not in s and '9' not in s:
        raise ValueError("Некорректно введено выражение")
    if '  ' in s:
        raise ValueError("Некорректно введено выражение")
    pattern = r'[0-9.][ ][0-9.]'
    z = findall(pattern, s)
    if len(z) > 0:
        raise ValueError("Некорректно введено выражение")
    while ' ' in s:
        s = s.replace(' ', '')
    i = 0
    state = 0
    balance = 0
    while i < len(s):
        if s[-1] not in '1234567890)':
            raise ValueError("Некорректно введено выражение")
        if s[i] in '1234567890':
            if state != 5:
                state = 1
                i += 1
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in '.':
            if state == 1:
                i += 1
                state = 2
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in '+-':
            if state == 0 or state == 1 or state == 4 or state == 5:
                i += 1
                state = 3
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in '(':
            balance += 1
            if state != 1 and state != 2 and state != 5:
                i += 1
                state = 4
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in ')':
            balance -= 1
            if state == 1 or state == 5:
                i += 1
                state = 5
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in '*/':
            if state == 1 or state == 5:
                i += 1
                state = 6
            elif state == 6:
                i += 1
                state = 7
            else:
                raise ValueError("Некорректно введено выражение")

        elif s[i] in '%':
            if state == 1 or state == 5:
                i += 1
                state = 8
            else:
                raise ValueError("Некорректно введено выражение")
        else:
            raise ValueError(f"Введен неверный символ: {s[i]}")
        if balance >= 0:
            pass
        else:
            raise ValueError("Некорректно введено выражение")
    if balance == 0:
        pass
    else:
        raise ValueError("Некорректно введено выражение9")
    return True
