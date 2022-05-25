from ast import Try

welcome_msg = "Let's add two numbers together!"
print(welcome_msg)
close = False

while close == False:
    first_num = input("\nEnter the first number: ")
    second_num = input("Enter the second number: ")
    try:
        first_num = int(first_num)
        second_num = int(second_num)
        add_result = first_num + second_num
        print("\nThe result is: " + str(add_result))  
        
        user_ans = input("\nWould you like to add two numbers again? 1 (No) 2 (Yes): ")
        if (user_ans == '1' or user_ans == 'no'):
            break
        elif (user_ans == '2'):
            continue
        else:
            print("\nIncorrect input. The program will restart.\n")
            print(welcome_msg)
            continue
    except:
        print("Incorrect input. Please make sure to enter whole numbers. \nFor example 1, 300 and 234")
           
print("\nThank you for using my program. The program will now close.")
close = True