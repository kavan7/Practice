#PART A 
num = int(input("Enter grid size: "))
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print((j) * i, end=' ')
    print()
#PART B
size = int(input("Enter pyramid size: "))
for j in range(1, size + 1):
    print(f"." * (size - j), end='')
    print(f"{j}" * j, end='')
    print()
    

    
   
   
        
