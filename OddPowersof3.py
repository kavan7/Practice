#Given an integer variable n, find the first n odd powers of 3
#if n=3,  output -> {3, 27, 243}

def firstnoddpowersof3(n):
    powersof3 = []
    power = 1
    while len(powersof3) < n:
        powersof3.append(3**power)
        power += 2

    return powersof3
    
n = int(input("Enter n: "))

oddpowers = firstnoddpowersof3(n)

print("First", n, "Odd powers of 3", oddpowers)
