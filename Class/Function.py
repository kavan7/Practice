#Kavan Abeyratne
#ICS3U1


def factorial(n):
    if n < 0:
        print("Please enter a positive integer.")
    product = 1
    for i in range(1, n + 1):
        product *= i


    print(f"The product of natural numbers from 1 to {n} is: {product}")



def calculator(num1, num2, operation):
    if operation == "a":
        result = num1 + num2
    elif operation == "s":
        result = num1 - num2
    elif operation == "m":
        result = num1 * num2
    elif operation == "d":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero.")
            return
    else:
        print("Invalid operation. Please use 'a' for addition, 's' for subtraction, 'm' for multiplication, 'd' for division.")
        return

    print(f"Result of {num1} {operation} {num2} is: {result}")



def is_prime_number(num):
    if num <= 1:
        print(f"{num} is not a prime number.")
        return

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return

    print(f"{num} is a prime number.")



