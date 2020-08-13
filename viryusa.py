def expr(val):
    val = list(val)
    stack = list()
    numb = ""
    while len(val) > 0:
        c = val.pop(0)
        if c in "0123456789":
            numb += c
        else:
            if numb != "":
                stack.append(num)
                numb = ""
            if c in "+-*/":
                stack.append(c)
            elif c == ")":
                num2 = stack.pop()
                op = stack.pop()
                num1 = stack.pop()
                if op == "+":
                    stack.append(str(float(num1) + float(num2)))
                elif op == "-":
                    stack.append(str(float(num1) - float(num2)))
                elif op == "*":
                    stack.append(str(float(num1) * float(num2)))
                elif op == "/":
                    stack.append(str(float(num1) / float(num2)))
    return stack.pop()

val = input()
print(eval(val))