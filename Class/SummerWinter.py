print('Hello. My name is Com Puter. What is your name?')
Name = input().capitalize()

print (f'It is good to meet you, {Name}.')
print ()
print('I would like to ask you a question.') 
print ()
print (f'Do you like winter or summer the best {Name}?') 
season =input ()

if season == ('summer'):
    print('I like summer the best as well')
    print('Do you ever find that summer is too hot?') 
    print('Please answer yes or no.')
    hot = input ()


    if hot  == ('no'):
        print ('Me either. You will never hear me complain') 
        print ('about the weather being too hot in the summer time.')
    elif hot ==('yes'):
        print ('''I find that interesting. You said that you find summer to be too hot but yet you also said that summer was your favourite time of year.''')
if season == ('winter'):
    print ('Don\'t you find winter too cold?')
    print ('Please answer yes or no.')
    cold =  input ()
    if cold == ('no'):  
            print ("I think you are crazy. I don't know how you stay warm") 
            print ()

print (f'It\'s been nice chatting with you {Name}. ')
print ('I hope we get the chance to chat again soon, ')
print (f'I must go now {Name}. Goodbye')