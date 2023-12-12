# PART A
min = int(input("Enter first number: "))
max = int(input("Enter last number: "))
sum = 0
product = 1
for i in range(min, max + 1):
    sum += i
    product *= i

print(f"Sum is {sum} ")
print(f"Product is {product}")
    

# PART B
length = int(input("Enter sequence length: "))
numbers = [0, 1]

for i, val in enumerate(range(length - 2)):
    numbers.append(numbers[i] + numbers[i + 1])

print(numbers)

# PART C

num = int(input("Enter number: "))
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print(factors)