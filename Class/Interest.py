#Kavan Abeyratne
#ICS3U1

def interestgrowth(sa, agr, tp):
   
    grdecimal = 1 + (agr / 100)
  
    future = sa * (grdecimal ** tp)
    
    return future

sa = float(input("Enter the starting amount (in dollars): "))
agr = float(input("Enter the annual growth rate (in percentage): "))
tp = int(input("Enter the time period (in years): "))

result = interestgrowth(sa, agr, tp)

print(f"The future value after {tp} years will be: ${result:.2f}")


def inputs():
    values = []
    while True:
        user_input = input("Enter a number (type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            value = float(user_input)
            values.append(value)
        except ValueError:
            print("Invalid input.")
    return values

def average_computer(values_list):
    if not values_list:
        return 0  
    total = sum(values_list)
    average = total / len(values_list)
    return average

input_values = inputs()

average = average_computer(input_values)

print(f"The average is: {average}")
