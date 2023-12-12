def romanint(rnum):
    valmap = {'I' : 1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    number = 0
    prevnum = 0
    for char in rnum:
        if char in valmap:
            if valmap[char] > prevnum:  
                number += valmap[char] - 2 * prevnum
            else:
                number += valmap[char]
        prevnum = valmap[char]

    return number

rnum = 'IV'
print(romanint(rnum))
