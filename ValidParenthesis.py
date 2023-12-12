def isValid(s):
    stack = []
    bracketmap = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracketmap.values():
            stack.append(char)
        else:
            if not stack or stack.pop() != bracketmap[char]:
                return False
            
        return stack
s = "()"
print(isValid(s))

