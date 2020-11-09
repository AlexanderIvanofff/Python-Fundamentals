def solution(row_data):
    data = row_data.split()
    return {
        data[i]: (int(data[i + 1]))
        for i in range(0, len(data), 2)
}


print(solution(input()))