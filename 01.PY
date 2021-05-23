
sum = 0
while(True):
    userinput = input("Enter the price or press q to quit:\n")
    if(userinput != 'q'):
        sum = sum + int(userinput) 
        print(f"your order so far: {sum}")
    else:
        print("Thanks for using our calculator")
        print(f"your total bill is: {sum}")
        break



