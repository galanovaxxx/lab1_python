import src.expr


def primary_function(s: list) -> [int, float]:
    """Функция проверяет, есть ли в списке скобки. Если да, то алгоритм повторяется,
    иначе выводит ответ"""
    if s:
        if '(' in s:
            return src.expr.expr_function(s)
        return s[0]

