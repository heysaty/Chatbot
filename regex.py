import re


def calculate(says):
    exp = list(re.findall("(\d*)([-|+|*|])(\d*)", says))

    if exp[0][1] == '-':
        return int(exp[0][0]) - int(exp[0][2]), [exp[0][0],exp[0][1],exp[0][2]]
    elif exp[0][1] == '+':
        return int(exp[0][0]) + int(exp[0][2]), [exp[0][0], exp[0][1], exp[0][2]]
    elif exp[0][1] == '*':
        return int(exp[0][0]) * int(exp[0][2]), [exp[0][0], exp[0][1], exp[0][2]]


