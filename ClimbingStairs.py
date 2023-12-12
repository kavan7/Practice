def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    odd_steps = 1
    even_steps = 2

    if n % 2 == 0:
        even_steps += odd_steps

    else:
        odd_steps += even_steps


    return even_steps if n % 2 == 0 else odd_steps