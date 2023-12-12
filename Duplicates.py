def isDup(nums):
    nums_set = set(nums)
    return len(nums_set) != len(nums)

while True:
    user_input = input("Enter numbers with no spaces (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        break
    
    nums = list(map(int, user_input))
    print(isDup(nums))
