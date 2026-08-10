#Evaluating expressions without using in-built functions,lists,tuples,sets.

def calculate(expression):

    num = ""
    result = 0
    op = "+"

    for ch in expression + "+":
        if ch.isdigit():
            num += ch
        else:
            if op == "+":
                result += int(num)
            elif op == "-":
                result -= int(num)

            op = ch
            num = ""

    print("Result =", result)


expression = input("Enter expression: ")
calculate(expression)
