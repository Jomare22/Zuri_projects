#Message entries to concat
msg1 = "\nEnter the number of an operation to perform:"
msg2 = "\nOption 1: Addition"
msg3 = "\nOption 2: Subtraction"
msg4 = "\nOption 3: Division"
msg5 = "\nOption 4: Multiplication"
msg6 = "\nOption 5: Modulus operation\nOption: "
init_msg = msg1 + msg2 + msg3 + msg4 + msg5 + msg6
welcome_msg = "Welcome to my simple calculator!"

close = False #variable used in the while loop
print(welcome_msg)

while close == False:
    operation = input(init_msg)
    selected_num = int(operation)
    
    if selected_num<=5 and selected_num <=5:
        try: #Check if a correct input(1-5) is selected
            num_1 = input("\nPlease enter the first number: ")
            num_2 = input("Please enter the the second number: ")            
        except: #When a valid option between 1 and 5 isn't selected
            print("\nInvalid input. Please enter only numbers in the following format: 4.6 and 100.\nLetters and special characters are not accepted.\n Let's restart.")
            continue
        #Addition
        if operation == "1":
            print("\nThe sum is " + str(float(num_1)+float(num_2)))
        #Subtraction
        elif operation == "2":
            print("\nThe difference is " + str(float(num_1)-float(num_2)))
        #Division
        elif operation == "3":
            print("\nThe result is " + str(float(num_1)/float(num_2)))
        #Multiplication
        elif operation == "4":
            print("\nThe product is " + str(float(num_1)*float(num_2)))
        #Modulus
        elif operation == "5":
            print("\nThe remainder is " + str(float(num_1)%float(num_2)))
        else: #When a number isn't entered
            print("\nInvalid input. Please enter only numbers in the following format: 4.6 and 100.\nLetters and special characters are not accepted.\n Let's restart.")
            continue
        
        #Ask to rerun the program
        user_ans = input("\nWould you like to perform another operation? 1 (No) 2 (Yes): ")
        if (user_ans == '1' or user_ans == 'No' or user_ans == 'no' or user_ans =='n'):
            print("\nThank you for using my simple calculator. The program will now close.")
            close = True #Closing the loop
        elif (user_ans == '2' or user_ans == 'Yes' or user_ans == 'yes' or user_ans == 'y'):
            continue
        else:
            print("\nIncorrect input. The program will restart.\n")
            print(welcome_msg)
            continue
    else:
        print("Invalid option. Please select a number between 1 and 5.\nLet's try again!\n")
        print(welcome_msg)
        continue