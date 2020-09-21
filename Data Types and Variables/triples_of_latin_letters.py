def solve(number):
    for i in range(number):
        for j in range(number):
            for k in range(number):
                print(f"{chr(i + 97)}{chr(j + 97)}{chr(k + 97)}")


solve(int(input()))