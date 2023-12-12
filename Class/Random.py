import random
num = random.randint(1, 100)
if num % 2 == 0:
    oddeven = "Even"
else:
    oddeven = "Odd"
numstr = str(num)
numstrl = len(numstr)
if num % 10 == 0:
    endten = "The number ends in 0"
else: 
    endten = "The number does not end in 0"
print("The number is " + str(num) )
print("The number is " + str(oddeven) )
print(str(endten))
print("The number has " + str(numstrl) + " Digits" )


studenthrs = random.randint(100, 500)
mark = random.uniform(80, )
if studenthrs > 250 and mark >= 90:
    print("You win a 2000$ scholarship")
elif studenthrs > 150 and mark == 80:
    print("You win a 800$ scholarship")