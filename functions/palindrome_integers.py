def is_palindrome(number_str):
    reversed_num = number_str[::-1]

    return True if reversed_num == number_str else False


nums = input().split(', ')

for num in nums:
    print(is_palindrome(num))