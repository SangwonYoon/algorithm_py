def merge_sort(list):
    result = []
    if len(list) == 1:
        return list
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right[0])
            right = right[1:]
        else:
            result.append(left[0])
            left = left[1:]
    if len(left) == 0:
        result += right
    else:
        result += left
    return result

print(merge_sort([3,4,5,1,2,10,7]))