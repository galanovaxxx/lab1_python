import src.add


def expr_function(s: list) -> [int, float]:
    """Функция убирает скобки, окаймляющие список, если скобки есть
    и список не пустой. Потом вызывает функцию add."""
    balance = 0 # проверка скобок
    flag = 1 # флаг для проверки, закрывается ли первая скобка
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
            s = s[1:-1] # удаляем скобки, если они окаймляют выражение
    return src.add.add_function(s)

