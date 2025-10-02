from src.check import check_function
from src.token import token_function
from src.expr import expr_function


def final(s):
  """ Функция выводит ответ, если число проходит проверку."""
    if check_function(s):
        s = token_function(s)
        k = expr_function(s)
        if '.' in str(k):
            if int(k) == k:
                return int(k)
        return k
    return 0
