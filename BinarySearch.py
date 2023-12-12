def binarySearch(s, target):
    left, right = 0, len(s - 1)
    while left <= right:
        mid = left + (right - left) // 2
        
        if [mid] == target:
            return [mid]
        elif target < mid:
            return target

print(binarySearch(s, target))

s = [1, 3, 5, 7, ]
target = 4