import src.pow


def mul_function(s: list) -> [int, float]:
    """Функция находит '*', или '/', или '//', или '%' аходящееся не в скобках и
    снова вызывает эту функцию от частей списка до и после найденых элементов.
    Если элементов в списке нет, вызывает другую функцию."""
    if '*' in s: # если в строке есть * 
        balance = 0
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '*':
                if balance == 0:
                    return mul_function(s[:x]) * mul_function(s[x + 1:]) # вызываем эту же функию от срезов списка до и после *
    if '/' in s: # если в строке есть /
        balance = 0
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '/':
                if balance == 0:
                    if mul_function(s[x + 1:]) != 0: # проверка нет ли деления на 0
                        return mul_function(s[:x]) / mul_function(s[x + 1:]) # вызываем эту же функию от срезов списка до и после /
                    else:
                        raise ValueError("Ошибка при делении")
    if '//' in s: # если в строке есть //
        balance = 0
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '//':
                if balance == 0:
                    if mul_function(s[x + 1:]) != 0 and int(mul_function(s[:x])) == mul_function(s[:x]) and int(mul_function(s[x + 1:])) == mul_function(s[x + 1:]): # проверка нет ли деления на 0 или // или % c нецелыми числами
                        return mul_function(s[:x]) // mul_function(s[x + 1:]) # вызываем эту же функию от срезов списка до и после //
                    else:
                        raise ValueError("Ошибка при делении")
    if '%' in s: # если в строке есть %
        balance = 0
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '%':
                if balance == 0:
                    if mul_function(s[x + 1:]) != 0 and int(mul_function(s[:x])) == mul_function(s[:x]) and int(mul_function(s[x + 1:])) == mul_function(s[x + 1:]): # проверка нет ли деления на 0 или // или % c нецелыми числами
                        return mul_function(s[:x]) % mul_function(s[x + 1:]) # вызываем эту же функию от срезов списка до и после //
                    else:
                        raise ValueError("Ошибка при делении")
    return src.pow.pow_function(s) # вызываем новую функцию, если нет *, /, //, %
