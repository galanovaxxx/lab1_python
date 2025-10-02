from src.add import add_function


def expr_function(s):
    """Функция убирает скобки, окаймляющие список, если скобки есть
    и список не пустой. Потом вызывает функцию add."""
    balance = 0
    flag = 1
    if '(' in s and s:
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            if s[i] == ')':
                balance -= 1
            if i > 0 and i != len(s) - 1:
                if balance == 0:
                    flag = 0
        if flag == 1:
            s = s[1:-1]
    return add_function(s)
