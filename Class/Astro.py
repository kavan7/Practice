signs = [' Aries March 21st - April 19th' , ' Taurus April 20th  – May 20th ' , ' Gemini May 21st – June 21st ' , ' Cancer June 22nd – July 22nd' , ' Leo July 23rd – August 22nd' , ' Virgo August 23rd – September 22nd' , ' Libra September 23rd – October 23' , ' Scorpio October 24th – November 22nd' , ' Sagittarius November 23rd – December 21st' , ' Capricorn December 22nd – January 19th' , ' Aquarius January 20th – February 18th' , ' Pisces February 19th – March 20th']
birthdays = ['March 21st - April 19th' , ' April 20th  – May 20th ' , ' May 21st – June 21st ' , ' June 22nd – July 22nd' , ' July 23rd – August 22nd' , ' August 23rd – September 22nd' , ' September 23rd – October 23' , ' October 24th – November 22nd' , ' November 23rd – December 21st' , ' December 22nd – January 19th' , ' January 20th – February 18th' , ' February 19th – March 20th']


for i, val in enumerate(birthdays):
    
    answer = input(("Does your birthday fall in " + str(val) +  "?" + " If so, please enter 'yes', else enter 'no' "))
    if answer == 'yes':
        print("You are a(n)" + signs[i] + "!")
        break
    else:
        continue 

    
    
