def isPalindrome(x):
        lis = []
        for i in str(x):
            lis.append(i)
        
        if lis[::-1] == lis:
            return True

        else:
            return False


x = 121

print(isPalindrome(x))