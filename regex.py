import re


def calculate(says):
    try:
        exp = list(re.findall("(\d*)([-|+|*|])(\d*)", says))

        if exp is not None:
            if exp[0][1] == '-':
                return int(exp[0][0]) - int(exp[0][2]), [exp[0][0], exp[0][1], exp[0][2]]
            elif exp[0][1] == '+':
                return int(exp[0][0]) + int(exp[0][2]), [exp[0][0], exp[0][1], exp[0][2]]
            elif exp[0][1] == '*':
                return int(exp[0][0]) * int(exp[0][2]), [exp[0][0], exp[0][1], exp[0][2]]
    except:
        pass
    try:
        exp = list(re.findall("(^.*?) (\d*).*?(\d.*)", says))

        if exp is not None:

            if exp[0][0] == 'subtract' or exp[0][0] == 'sub':
                return int(exp[0][1]) - int(exp[0][2]), [exp[0][1], '-', exp[0][2]]
            elif exp[0][0] == 'add' or exp[0][0] == 'addition' or exp[0][0] == 'sum':
                return int(exp[0][1]) + int(exp[0][2]), [exp[0][1], '+', exp[0][2]]
            elif exp[0][0] == 'multiply' or exp[0][0] == 'mul':
                return int(exp[0][1]) * int(exp[0][2]), [exp[0][1], '*', exp[0][2]]
    except:
        pass



