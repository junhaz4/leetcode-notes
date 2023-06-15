class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # time complexity: o(N)
        # space complextity: o(N)
        stack = []
        for t in tokens:
            if t not in ("+","-","*","/"):
                stack.append(t)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(eval(f'{num2}{t}{num1}')))
        return int(stack.pop())

# method 2 using lambda function
def evalRPN( tokens: list[str]) -> int:
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }

    stack = []
    for token in tokens:
        if token in operations:
            number_1 = stack.pop()
            number_2 = stack.pop()
            operation = operations[token]
            stack.append(operation(number_2, number_1))
        else:
            stack.append(int(token))
    return stack.pop()