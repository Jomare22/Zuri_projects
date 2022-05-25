#Message entries to concat
msg1 = "\nEnter the number of an operation to perform:"
msg2 = "\nOption 1: Addition"
msg3 = "\nOption 2: Subtraction"
msg4 = "\nOption 3: Division"
msg5 = "\nOption 4: Multiplication"
msg6 = "\nOption 5: Modulus operation\nOption: "
init_msg = msg1 + msg2 + msg3 + msg4 + msg5 + msg6

close = False #variable used in the while loop

welcome_msg = "Welcome to my simple calculator!"

print(welcome_msg)

while close == False:
    operation = input(init_msg)
        
    try: #Check if a correct input(1-5) is selected
        #Addition
        if operation == "1":
            num_1 = input("\nPlease enter the first number: ")
            num_2 = input("Please enter the the second number: ")
            print("\nThe sum is " + str(float(num_1)+float(num_2)))
            #Ask to rerun the program
            user_ans = input("\nWould you like to perform another operation? 1 (No) 2 (Yes): ")
            if (user_ans == '1'):
                break
            elif (user_ans == '2'):
                continue
            else:
                print("\nIncorrect input. The program will restart.\n")
                print(welcome_msg)
                continue
        #Subtraction
        elif operation == "2":
            num_1 = input("\nPlease enter the first number: ")
            num_2 = input("Please enter the the second number: ")
            print("\nThe difference is " + str(float(num_1)-float(num_2)))
            #Ask to rerun the program
            user_ans = input("\nWould you like to perform another operation? 1 (No) 2 (Yes): ")
            if (user_ans == '1'):
                break
            elif (user_ans == '2'):
                continue
            else:
                print("\nIncorrect input. The program will restart.\n")
                print(welcome_msg)
                continue
        #Division
        elif operation == "3":
            num_1 = input("\nPlease enter the first number: ")
            num_2 = input("Please enter the the second number: ")
            print("\nThe result is " + str(float(num_1)/float(num_2)))
            #Ask to rerun the program
            user_ans = input("\nWould you like to perform another operation? 1 (No) 2 (Yes): ")
            if (user_ans == '1'):
                break
            elif (user_ans == '2'):
                continue
            else:
                print("\nIncorrect input. The program will restart.\n")
                print(welcome_msg)
                continue
        #Multiplication
        elif operation == "4":
            num_1 = input("\nPlease enter the first number: ")
            num_2 = input("Please enter the the second number: ")
            print("\nThe product is " + str(float(num_1)*float(num_2)))
            #Ask to rerun the program
            user_ans = input("\nWould you like to perform another operation? 1 (No) 2 (Yes): ")
            if (user_ans == '1'):
                break
            elif (user_ans == '2'):
                continue
            else:
                print("\nIncorrect input. The program will restart.\n")
                print(welcome_msg)
                continue
        #Modulus
        elif operation == "5":
            num_1 = input("\nPlease enter the first number: ")
            num_2 = input("Please enter the the second number: ")
            print("\nThe remainder is " + str(float(num_1)%float(num_2)))
            #Ask to rerun the program
            user_ans = input("\nWould you like to perform another operation? 1 (No) 2 (Yes): ")
            if (user_ans == '1'):
                break
            elif (user_ans == '2'):
                continue
            else:
                print("\nIncorrect input. The program will restart.\n")
                print(welcome_msg)
                continue 
        else: #When a number isn't entered
            print("\nInvalid entry. Please enter a number from 1 to 5.")
            continue
    except: #When a valid option between 1 and 5 isn't selected
        print("\nInvalid input. Please enter only numbers in the following format: 4.6 and 100.\nLetters and special characters are not accepted.\n Let's restart.")
        continue
print("\nThank you for using my simple calculator. The program will now close.")
close = True #Closing the loop

