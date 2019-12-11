import re
"""
过程：（最内部的括号->先乘除，替换->整理表达式->加减)->替换
"""


def multiply_divide(exp):
    # 计算乘除
    if '/' in exp:
        a, b = exp.split('/')
        return str(float(a)/float(b))
    if '*' in exp:
        a, b = exp.split('*')
        return str(float(a)*float(b))


def deal_with(expr):
    # 整理表达式
    expr = expr.replace('++', '+')
    expr = expr.replace('+-', '-')
    expr = expr.replace('--', '+')
    expr = expr.replace('-+', '-')
    return expr


def add(expr):
    # 计算加减，减法的实质式加法
    ret = re.findall('-?\d+\.?\d?', expr)
    sum = 0
    for i in ret:
        sum += float(i)
    return str(sum)


def expr_no_bracket(expr):
    # 计算括号内的值
    expr = expr.strip('()')
    # print(expr)
    # 计算
    while 1:
        ret = re.search('\d+\.?\d*[*/]-?\d+\.?\d*', expr)
        if ret:
            expr_son = ret.group()
            # print(expr_son)
            new_expr = multiply_divide(expr_son)
            expr = expr.replace(expr_son, new_expr)     # 替换
            expr = deal_with(expr)  # 整理
        else:   # 没有括号
            expr = add(expr)
            return expr


def calculate_main(expr):
    # 取空格
    expression = expr.replace(' ', '')
    # print(expression)
    while 1:
        ret = re.search('\([^()]+\)', expression)
        if ret:
            expr_brackets = ret.group()
            # print(expr_brackets)
            new_exp = expr_no_bracket(expr_brackets)
            expression = expression.replace(expr_brackets, new_exp)     # 求王括号内部，替换
            # print(new_exp)
            # print(expression)
        else:       # 没有括号
            ret = expr_no_bracket(expression)
            return ret


while 1:
    print('请输入表达式，按q退出!>')
    expression = input('>>')
    if expression == 'q':
        break
    ret = calculate_main(expression)
    print(ret)


# expression = '1 - 2 * ( (60-30 +(6-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'