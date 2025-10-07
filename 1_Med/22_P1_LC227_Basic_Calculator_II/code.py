# 227. Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/description/

def calculate(s: str) -> int:
    # ChatGPT's code: Stack implementation
    s = s.replace(" ", "")
    stack = []
    num = 0
    op = '+'
    
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        
        if ch in '+-*/' or i == len(s) - 1:
            # work with the previous operation first then do the new operation
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack[-1] = stack[-1] * num
            elif op == '/':
                stack[-1] = int(stack[-1] / num)
            op = ch
            num = 0

    return sum(stack)


    # My code
    history = [0]
    s = [i for i in s if i!=" "]
    for element in s:
        if element.isdigit():
            if isinstance(history[-1], int):
                history[-1] = history[-1]*10 + int(element)
            else:
                history.append(int(element))
        else:
            history.append(element)
    del s
    while True:
        if '*' not in history and '/' not in history:
            break

        current_op = None
        if '*' in history and '/' in history:
            if history.index('*') < history.index('/'):
                current_op = '*'
            else:
                current_op = '/'
        elif '*' in history:
            current_op = '*'
        else:
            current_op = '/'

        if current_op == '/':
            dv = history.index(current_op)
            calc = int(history[dv - 1] / history[dv + 1])
            history[dv - 1] = calc
            del history[dv:dv + 2]
        
        if current_op == '*':
            mul = history.index(current_op)
            calc = history[mul - 1] * history[mul + 1]
            history[mul - 1] = calc
            del history[mul:mul + 2]
    
    while True:
        if '+' not in history and '-' not in history:
            break

        current_op = None
        if '+' in history and '-' in history:
            if history.index('+') < history.index('-'):
                current_op = '+'
            else:
                current_op = '-'
        elif '+' in history:
            current_op = '+'
        else:
            current_op = '-'
        
        if current_op == '+':
            dv = history.index(current_op)
            calc = int(history[dv - 1] + history[dv + 1])
            history[dv - 1] = calc
            del history[dv:dv + 2]
        
        if current_op == '-':
            mul = history.index(current_op)
            calc = history[mul - 1] - history[mul + 1]
            history[mul - 1] = calc
            del history[mul:mul + 2]

    return history[0]

s = "1+2*5/3+6/4*2"
print(calculate(s))