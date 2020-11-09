from collections import defaultdict

count_words = defaultdict(int)


def solution(words):
    for word in words:
        count_words[word.lower()] += 1

    return ' '.join([word for word, count in count_words.items() if count % 2 != 0])


print(solution(input().split()))