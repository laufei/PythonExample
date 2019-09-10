# coding: utf-8

def three_sum_1(list, target):
    list_len = len(list)
    for i in range(list_len-2):
        for j in range(i+1, list_len-1):
            for k in range(j+1, list_len):
                tmp = sum([list[i], list[j], list[k]])
                if tmp == target:
                    return i, j, k
    return None

def three_sum_2(nums, targe):
    result = set()
    li_len = len(nums)
    for i in range(li_len - 1):
        dic = {}
        for j in range(i+1, li_len):
            a = nums[i]
            b = nums[j]
            c = targe - a - b
            if c not in dic:
                dic[a] = i
                dic[b] = j
            else:
                result.add((i, dic[c], j))
    return map(list, result)

if __name__ == "__main__":
    nums = [7, 5, 1, 8, 6, 4, 9]
    print three_sum_1(nums, 17)
    print three_sum_2(nums, 17)