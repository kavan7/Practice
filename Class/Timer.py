import time

timer = int(input("How long do you want the timer to last for (In seconds): "))

while True:
    print(timer)
   
    timer -= 1
    time.sleep(1)
    print("... 1 second later")
    if timer == 0:
        print("!!! TIME UP !!!")
        
        time.sleep(3)
        dismiss = input("Dismiss timer? You have five seconds before timer continues. Type 'ok': ")
        
        if dismiss.lower() == 'ok':
            print("Ok thanks for using my timer.")
            break
        elif dismiss.lower() != 'ok':
            while True:
                for i in range(3):
                    print("!!! TIME UP !!!")
                    time.sleep(1)
                dismiss = input("Dismiss timer? You have five seconds before timer continues. Type 'ok': ")
        
                if dismiss.lower() == 'ok':
                    print("Ok thanks for using my timer.")
                    exit()

                
                    
                elif dismiss.lower() != 'ok':
                    continue

       

   
    
            
    

    