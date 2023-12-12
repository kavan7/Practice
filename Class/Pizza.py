print ('Do you have time to answer a few questions for me?')
question = input("Please answer yes or no: " )

if question=='yes':
    print("Fantastic")
    like = input("Do you like pizza? Yes or No?: ")

    if like == 'yes':
        print('I like pizza as well.')
    elif like == 'no':
        print('Thats too bad because I like pizza.')
elif question == 'no':
    print("Okay. Thanks anyway.")

print("Goodbye")
