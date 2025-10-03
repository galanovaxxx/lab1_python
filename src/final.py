import src.check
import src.token
import src.expr


def final_function(s: list) -> [int, float]:
    if src.check.check_function(s):
        s = src.token.token_function(s)
        k = src.expr.expr_function(s)
        if '.' in str(k):
            if int(k) == k:
                return int(k)
        return k
    return 0
