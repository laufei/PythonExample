# coding: utf-8

from collections import Counter

source = [1, 3, 8, 9, 15, 12, 15, 3, 3, 9]
def get_2dup(source):
    result = {}
    for i in source:
        result[i] = result.get(i, 0) + 1
    return [k for k, v in result.items() if v ==2]

def get_2dup_counter(source):
    result = Counter(source)
    return [k for k, v in result.items() if v == 2]

# # 不使用 python 标准库
# def get_2dup(candidates):
#     if len(candidates) <= 1:
#         return []
#     count_result = {}
#     for candidate in candidates:
#         count_result[candidate] = count_result.get(candidate, 0) + 1
#     return [k for k, v in count_result.items() if v == 2]
#
# # 使用Counter
# def get_2dup_counter(candidates):
#     if len(candidates) <= 1:
#         return []
#     count_result = Counter(candidates)
#     return [k for k, v in count_result.items() if v == 2]

if __name__ == '__main__':
    print(get_2dup(source))
    print(get_2dup([1]))
    print(get_2dup([]))
    print(get_2dup_counter(source))
    print(get_2dup_counter([]))
    print(get_2dup_counter([9]))