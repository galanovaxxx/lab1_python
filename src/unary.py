import src.primary
import src.expr


def unary_function(s: list) -> [int, float]:
    """Функция работает с унарными знаками. Если '+', удаляет его, если '-', удаляет его
    и умножает следующее за ним число на (-1)."""
    print(s)
    if s: # если s не пустой 
        if s[0] == '+': # если первый символ +
            s.pop(0) # удаляем +
            return src.expr.expr_function(s) # вызываем функцию снова
        if s[0] == '-': # если первый символ -
            s.pop(0) # удаляем -
            return -(src.expr.expr_function(s)) # вызываем отрицательную функцию от этой функции
    return src.primary.primary_function(s) # вызываем следующую функцию
