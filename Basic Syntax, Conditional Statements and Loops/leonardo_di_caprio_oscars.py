def solve(number):
    if number == 88:
        return f'Leo finally won the Oscar! Leo is happy'
    elif number == 86:
        return f'Not even for Wolf of Wall Street?!'
    elif number != 88 and 86 and number < 88:
        return f'When will you give Leo an Oscar?'
    elif number > 88:
        return f'Leo got one already!'


print(solve(int(input())))
