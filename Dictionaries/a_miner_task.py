from collections import defaultdict


def solution(item):
    total_idem = defaultdict(int)

    while item != 'stop':
        count_item = int(input())
        total_idem[item] += count_item

        item = input()

    for k, n in total_idem.items():
        print(f'{k} -> {n}')


solution(input())