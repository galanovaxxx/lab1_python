import unary


def pow_function(s):
    """Функция находит '**', находящееся не в скобках и снова вызывает эту функцию
    от частей списка до и после '**'. Если '**' нет в списке, вызывает другую функцию"""
    if '**' in s:
        balance = 0
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '**':
                if balance == 0:
                    return pow_function(s[:x]) ** pow_function(s[x + 1:])

    return unary.unary_function(s)
