import src.check
import src.token
import src.expr


def final_function(s: list) -> [int, float]:
    """Функция объединяет все предыдущие функции"""
    if src.check.check_function(s): # если выражение введено корректно
        s = src.token.token_function(s) # токенизируем
        k = src.expr.expr_function(s) # присваиваем k значение функции (число)
        if '.' in str(k): # проверяем есть ли точки 
            if int(k) == k: # если число целое, переводим в int на случай, если целое число во float
                return int(k)
        return k # если нет точек или число дробное
    return 0
