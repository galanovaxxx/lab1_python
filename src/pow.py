import src.unary


def pow_function(s: list) -> [int, float]:
    """Функция находит '**', находящееся не в скобках и снова вызывает эту функцию
    от частей списка до и после '**'. Если '**' нет в списке, вызывает другую функцию"""
    if '**' in s: #если в списке есть **
        balance = 0
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '**':
                if balance == 0: # если ** не в скобках
                    return pow_function(s[:x]) ** pow_function(s[x + 1:]) # вызываем эту же функцию до и после **

    return src.unary.unary_function(s) # если нет ** вызываем другую функцию
