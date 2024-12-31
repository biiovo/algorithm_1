def contains_subsequence(x, y, good):
    target = "suanfa"
    target_len = len(target)
    target_index = 0
    for row in range(x):
        for char in good[row]:
            if char == target[target_index]:
                target_index += 1
                if target_index == target_len:
                    return "YES"
    return "NO"
x, y = map(int, input().split())
good = [input().strip() for _ in range(x)]
result = contains_subsequence(x, y, good)
print(result)
