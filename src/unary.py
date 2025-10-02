from src.primary import primary_function


def unary_function(s):
    """Функция работает с унарными знаками. Если '+', удаляет его, если '-', удаляет его
    и умножает следущее за ним число на (-1)."""
    if s:
        if s[0] == '+' and (type(s[1]) == int or type(s[1]) == float):
            s.pop(0)
        if s[0] == '-':
            s.pop(0)
            s[0] = s[0] * (-1)
        if s:
            x = 0
            while x > len(s):
                if s[x] == '(':
                    if s[x + 1] == '+':
                        s.pop(x + 1)
                    if s[x + 1] == '-':
                        s.pop(x + 1)
                        s[x + 1] = s[x + 1] * (-1)
                    x += 1
    return primary_function(s)
