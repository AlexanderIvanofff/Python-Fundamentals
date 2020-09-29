def number_beggars(number_str, count):
    nums = []
    for num in number_str:
        nums.append(int(num))

    result = [0] * count

    for i in range(len(nums)):
        index = i % count
        result[index] += nums[i]
    return result


print(number_beggars(input().split(', '), int(input())))
