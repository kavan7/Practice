def twosum(s, target):
    hmap = {}

    for i, val in enumerate(s):
        diff = target - val
        if diff in hmap:
            return [hmap[diff], i]
        
        hmap[val] = i

    
s = [3, 6, 2, 9, 11]
target = 11

print(twosum(s, target))

