uniquechars = ['.', '?', '!', ';', ':','-']
sentencechars = set()

sentence = input("Enter sentence: ")

for char in sentence:
    if char in uniquechars:
        sentencechars.add(char)

print(sentencechars)


print("_________________")
print()
print("PART 2")
charone = input("Enter first letter: ")
words = set()
print((f"Enter as many 5 letter words that start with {charone} "))
while True:
    word = input("Word: ")
    word.lower()
    if len(word) == 5 and word[0] == charone:
        
            words.add(word)
            if len(words) == 1:
                print(f"You have one word")
            else:
                print(f"You have {len(words)} words ")
        
            print("You have already entered that word.")

    elif word == 'quit':
        break

    else:
        print(f"Make sure your word is 5 letters and starts with {charone} ")