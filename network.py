from calc import *

def poop(p, dic):
    if not p:
        return dic
    elif isassignment(p):
        dic[eval_expr(first_statement(p)), poop(rest_statements(p))
        
            

############################## Assignment functions ######################
def assigner(assg_stmnt):
    

def eval_expr(expr):
    if isbinary(expr):
        return binary_calc(expr)
    elif isconstant(expr) or isvariable(expr):
        return expr

def binary_calc(binexpr):
    if binary_operator(binexpr) == '+':
        return eval_expr(binary_left(binexpr)) + eval_expr(binary_right(binexpr))
    elif binary_operator(binexpr) == '-':
        return eval_expr(binary_left(binexpr)) - eval_expr(binary_right(binexpr))
    elif binary_operator(binexpr) == '/':
        return eval_expr(binary_left(binexpr)) / eval_expr(binary_right(binexpr))
    elif binary_operator(binexpr) == '*':
        return eval_expr(binary_left(binexpr)) * eval_expr(binary_right(binexpr))
    
###########################

def eval_program(calc_prog, optional = {}):
    if isprogram(calc_prog): #check if calc prog is a valid prog
        if isstatements(program_statements(calc_prog)):
            if isassignment(first_statement(program_statements(calc_prog))):
                optional[first_statement(program_statements(calc_prog))[1]] = eval_expr(first_statement(program_statements(calc_prog))[2])
                return optional
                                                               
                    
            
            