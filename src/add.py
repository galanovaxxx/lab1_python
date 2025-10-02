from src.mul import mul_function


def add_function(s):
    """Функция находит '+' или '-' находящееся не в скобках и снова
    вызывает эту функцию от частей списка до и после найденых элементов.
    Если элементов в списке нет, вызывает другую функцию."""
    balance = 0
    if '+' in s[1:]:
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '+':
                if balance == 0:
                    return add_function(s[:x]) + add_function(s[x + 1:])

    if '-' in s[1:]:
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '-':
                if balance == 0:
                    return add_function(s[:x]) - add_function(s[x + 1:])
    return mul_function(s)
