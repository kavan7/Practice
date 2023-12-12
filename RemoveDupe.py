def removeDupe(n):
    speciallist = []
    for i in range(len(n)):
        if i == 0 or n[i] != n[i - 1]:
            speciallist.append(n[i])
    return speciallist

n = [1, 1, 3]
print(removeDupe(n))