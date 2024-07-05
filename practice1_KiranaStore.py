#Write a python program which will keep addding a stream of numbers inputted 
# by user. The adding stops as soon as user presses q key on the keyboard.
sum = 0
while(True):
    userInput = input("Enter the price or press q to exit::")
    
    if(userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order so far is {sum}")
    else:
        print(f"Your total bill amount is {sum}\n Thank you for visiting our shop!!")    
        break
