from src.expr import expr_function


def primary_function(s):
    """Функция проверяет, есть ли в списке скобки. Если да, то алгоритм повторяется,
    иначе выводит ответ"""
    if s:
        if '(' in s:
            return expr_function(s)
        return s[0]
