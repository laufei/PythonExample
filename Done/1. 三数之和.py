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

def three_sum_2(list, targe):
    list_len = len(list)
    for i in range(list_len-1):
        tmp = {}
        for j in range(i+1, list_len):
            a = list[i]
            b = list[j]
            c = targe - a - b
            if c not in tmp:
                tmp[a] = i
                tmp[b] = j
            else:
                return i, tmp[c], j

if __name__ == "__main__":
    list = [7, 5, 1, 9]
    print three_sum_1(list, 17)
    print three_sum_2(list, 17)