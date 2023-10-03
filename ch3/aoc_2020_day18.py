equation = "(" + ") + (".join(
    [l.strip() for l in open("input.txt").readlines()]) + ")"

equation = equation.replace('(', "( ").replace(')', " )")

# print(equation)
eqops = [int(c) if c[0].isdigit() else c for c in equation.split()]

PRECEDENCE = lambda o: "*+".index(o)  # + higher than *


#[2, 3, 4, 5, * + *]
def to_postfix_precedence(eq, p1=False):
    oqueue = []
    opstack = []
    for v in eq:
        if isinstance(v, int):
            oqueue.append(v)
        else:
            if (v == '('):
                opstack.append(v)
            elif (v == ")"):
                while len(opstack) and opstack[-1] != '(':
                    oqueue.append(opstack.pop())
                opstack.pop()
            else:  # Operator
                while len(opstack) and opstack[-1] != '(':
                    if p1 or (PRECEDENCE(opstack[-1]) > PRECEDENCE(v)):
                        oqueue.append(opstack.pop())
                    else:
                        break
                opstack.append(v)
    oqueue += reversed(opstack)
    return oqueue


def eval_postfix(pfx):
    s = []
    for v in pfx:
        if isinstance(v, int):
            s.append(v)
        else:
            s.append(eval(f"{s.pop()}{v}{s.pop()}"))

    return s[-1]


print(f"Part One: {eval_postfix(to_postfix_precedence(eqops, True))}")
print(f"Part Two: {eval_postfix(to_postfix_precedence(eqops, False))}")
