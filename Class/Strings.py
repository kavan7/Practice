q1 = 'What are your hobbies?'
q2 = 'What are your favorite books/movies/TV shows?'
q3 = 'Where did you grow up?'
q4 = "What's your favorite place you've ever visited?"
q5 = "What's your favorite food?"

a1 = "Some of mine are rock climbing and skiing."
a2 = 'I love "The Lord of the Rings" movie trilogy, and my favorite TV show is "The Office.'
a3 = "I was born and raised in Toronto, ON, and I've visited many cool places -- I really loved Edinburgh, Scotland, and hope to go back there some day."
a4 = "I also have a brother who lives in Waterloo, and while we don't see each other as much as we'd like, I'd still describe ourselves as close."
a5 = "As for my favorite foods, can I say anything chocolate-covered? ;)"


input1 = input(q1)
print("Wow thats really cool! As your python program I've never partook in  " + input1 + " " + a1)
input2 = input(q2)
print("Good to know!" + input2 + " sounds awesome!" + a2)
input3 = input(q3)
print("Interesting!" + input3 + " looks really cool!" + a3)
input4 = input(q4)
print("I can see why!" + input4 + " seems really beautiful." + a4)
input5 = input(q5)
print("Delicious!" + input5 + " tastes amazing" + q5)

#Second Assignment
stack = []
for i in range(3):
    str = input("Enter string: ")
    length = len(str)
    stack.append(length)
    print(length)
ans = sum(stack)
print(ans)



