import src.primary
import src.expr


def unary(s):
    """Функция работает с унарными знаками. Если '+', удаляет его, если '-', удаляет его
    и умножает следующее за ним число на (-1)."""
    print(s)
    if s:
        if s[0] == '+':
            s.pop(0)
            return src.expr.expr_function(s)
        if s[0] == '-':
            s.pop(0)
            return -(src.expr.expr_function(s))
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
    print(s)
    return src.primary.primary_function(s)
