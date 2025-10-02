import pow


def mul_function(s):
    """Функция находит '*', или '/', или '//', или '%' аходящееся не в скобках и
    снова вызывает эту функцию от частей списка до и после найденых элементов.
    Если элементов в списке нет, вызывает другую функцию."""
    if '*' in s:
        balance = 0
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '*':
                if balance == 0:
                    return mul_function(s[:x]) * mul_function(s[x + 1:])
    if '/' in s:
        balance = 0
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '/':
                if balance == 0:
                    if mul_function(s[x + 1:]) != 0:
                        return mul_function(s[:x]) / mul_function(s[x + 1:])
                    else:
                        raise ValueError("Ошибка при делении")
    if '//' in s:
        balance = 0
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '//':
                if balance == 0:
                    if mul_function(s[x + 1:]) != 0 and int(mul_function(s[:x])) == mul_function(s[:x]) and int(mul_function(s[x + 1:])) == mul_function(s[x + 1:]):
                        return mul_function(s[:x]) // mul_function(s[x + 1:])
                    else:
                        raise ValueError("Ошибка при делении")
    if '%' in s:
        balance = 0
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == '%':
                if balance == 0:
                    if mul_function(s[x + 1:]) != 0 and int(mul_function(s[:x])) == mul_function(s[:x]) and int(mul_function(s[x + 1:])) == mul_function(s[x + 1:]):
                        return mul_function(s[:x]) % mul_function(s[x + 1:])
                    else:
                        raise ValueError("Ошибка при делении")
    return pow.pow_function(s)
