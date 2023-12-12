def isValid(s, t ):
    return sorted(s) == sorted(t)




while True:
    s = str(input("Enter first string: "))

    t = str(input("Enter second string: "))

    print(isValid(s, t))