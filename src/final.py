import check
import token
import expr


def final_function(s):
    if check.check_function(s):
        s = token.token_function(s)
        k = expr.expr_function(s)
        if '.' in str(k):
            if int(k) == k:
                return int(k)
        return k
    return 0
