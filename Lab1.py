print("Hello world")

def func(number1: float,number2: float, oper: str):
    add = "add"
    sub = "sub"
    mult = "mult"
    div = "div"
    result = 0.0
    if oper == add:
        result = number1 + number2
    if oper == sub:
        result = number1 - number2
    if oper == mult:
        result = number1 * number2
    if oper == div:
        result = number1 / number2
    return result

print(func(12.5, 45.0, "div"))
