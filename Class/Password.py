#PART A 
special = ['!', '@', '#', '-']
nums = ['1', '2']

while True:
    num = False
    specialchar = False

    pswd = input("Enter password: ")
    confirm = input("Confirm password: ")

    if confirm != pswd:
        print("Your password does not match")
    else:
        if len(pswd) > 7:
            for i in pswd:
                if i in special:
                    specialchar = True
                if i in nums:
                    num = True

            if not specialchar:
                print("Your password is missing a special character")

            if not num:
                print("Your password needs a number")

            if num and specialchar:
                print("Your password is valid!")
                break  
        else:
            print("Your password is not 8 characters long")
            
#PART B

vowel = ['a', 'e', 'i', 'o', 'u']
a = 0
e = 0
ii = 0 
o = 0 
u = 0
sent = input("Enter string: ")
for i in sent:
    if i in vowel[0]:
        a += 1
    if i in vowel[1]:
        e += 1
    if i in vowel[2]:
        ii +=1
    if i in vowel[3]:
        o += 1
    if i in vowel[4]:
        u += 1

print(f"a = {a} \ne = {e} \ni = {ii} \no = {o} \nu = {u}")
        

        