import operator

input_operator = input()
first_num = int(input())
second_num = int(input())


def solve(a, b, operation):
    operation_fn = None
    if operation == 'multiply':
        operation_fn = operator.mul
    elif operation == 'divide':
        operation_fn = operator.truediv
    elif operation == 'add':
        operation_fn = operator.add
    elif operation == 'subtract':
        operation_fn = operator.sub

    return operation_fn(a, b)


print(int(solve(first_num, second_num, input_operator)))