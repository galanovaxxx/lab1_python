from check import check_function
from token import tokenization
from calculator import expr


def final(s):
    if check_function(s): # если выражение введено корректно
        s = tokenization(s) # токенизируем
        k = expr(s)
        if '.' in str(k):
            if int(k) == k:
                return int(k) # возвращаем int от числа с точкой, если оно целое
        return k
    return 0
