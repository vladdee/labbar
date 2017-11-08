from calc import *

############################## Assignment functions ######################
def eval_expr(expr, dic):
    """
    Function recieves an expression, checks if it's a binexpr, if so,
    calls binary_calc and returns it's value, if the value's already been
    assigned it just takes it from there instead of treating it as just a
    string.
    """
    if isbinary(expr):
        return binary_calc(expr, dic)
    elif isconstant(expr):
        return expr
    elif isvariable(expr):
        if expr in dic:
            return dic[expr]
        else:
            return expr

def binary_calc(binexpr, dic):
    """
    Function recieves a binexpr and first evaluates the operator then calls
    on it self semi-recursively via the eval_expr function. It finally returns
    the value of the binary expression.
    """
    if binary_operator(binexpr) == '+':
        return eval_expr(binary_left(binexpr), dic) + eval_expr(binary_right(binexpr), dic)
    elif binary_operator(binexpr) == '-':
        return eval_expr(binary_left(binexpr), dic) - eval_expr(binary_right(binexpr), dic)
    elif binary_operator(binexpr) == '/':
        return eval_expr(binary_left(binexpr), dic) / eval_expr(binary_right(binexpr), dic)
    elif binary_operator(binexpr) == '*':
        return eval_expr(binary_left(binexpr), dic) * eval_expr(binary_right(binexpr), dic)

 # fråga carl om bättre sätt att föra vidare dictionaryn
###########################

def eval_program(calc_prog, optional = {}):
    if isprogram(calc_prog) and isstatements(program_statements(calc_prog)): #check if calc prog is a valid prog
        for stmnt in program_statements(calc_prog):
            if isassignment(stmnt):
                optional[stmnt[1]] = eval_expr(stmnt[2], optional)
    return optional
