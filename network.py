from calc import *

############################## General functions #########################
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

def parter(stmnts, dic):
    for stmnt in stmnts:
        if isassignment(stmnt):
            optional = assigner(stmnt, dic)
        elif isinput(stmnt):
            optional = inputter(stmnt, dic)
        elif isoutput(stmnt):
            outputter(stmnt, dic)
        elif isrepetition(stmnt):
            while_conditioner(stmnt, dic)
        elif isselection(stmnt):
            if_conditioner(stmnt, dic)
############################## Assignment functions ######################
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

def assigner(stmnt, dic):
    dic[stmnt[1]] = eval_expr(stmnt[2], dic)
    return dic
############################## Input functions ###########################
def inputter(stmnt, dic):
    dic[stmnt[1]] = eval(input(("Enter value for %s: ") % stmnt[1]))
    return dic
############################## Output functions ##########################
def outputter(stmnt, dic):
    if stmnt[1] in dic:
        print (dic[stmnt[1]])
    else:
        print (stmnt[1])
############################## Repetition functions #######################
def while_conditioner(stmnt, dic):
    if condition_operator(stmnt[1]) == '<':
        while eval_expr(stmnt[1][0], dic) < eval_expr(stmnt[1][2], dic):
            parter(stmnt[2:], dic)
    elif condition_operator(stmnt[1]) == '>':
        while eval_expr(stmnt[1][0], dic) > eval_expr(stmnt[1][2], dic):
            parter(stmnt[2:], dic)
    elif condition_operator(stmnt[1]) == '=':
        while eval_expr(stmnt[1][0], dic) == eval_expr(stmnt[1][2], dic):
            parter(stmnt[2:], dic)
############################## Selection functions ########################
def if_conditioner(stmnt, dic):
    if condition_operator(stmnt[1]) == '<':
        if eval_expr(stmnt[1][0], dic) < eval_expr(stmnt[1][2], dic):
            parter(stmnt[2:], dic)
    elif condition_operator(stmnt[1]) == '>':
        if eval_expr(stmnt[1][0], dic) > eval_expr(stmnt[1][2], dic):
            parter(stmnt[2:], dic)
    elif condition_operator(stmnt[1]) == '=':
        if eval_expr(stmnt[1][0], dic) == eval_expr(stmnt[1][2], dic):
            parter(stmnt[2:], dic)
############################## Final function
def eval_program(calc_prog, optional = {}):
    if isprogram(calc_prog) and isstatements(program_statements(calc_prog)): #check if calc prog is a valid prog
        parter(program_statements(calc_prog), optional)
    return optional
