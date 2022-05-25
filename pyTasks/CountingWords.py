welcome_message = "Welcome to my word counter."
print(welcome_message)

close = False

while close == False:
    user_input = input("\nPlease enter a sentence: ")
    user_input = user_input.strip(' ')
    
    space_count = 0

    for character in user_input:
        if character == " ":
            space_count = space_count +1
        
    number_of_words = space_count +1
    print("\nThe sentence entered is: "+ user_input)
    print("The number of words is: " + str(number_of_words))
    
    user_ans = input("\nWould you like to enter another sentence? 1 (No) 2 (Yes): ")
    if (user_ans == '1' or user_ans == 'no' or user_ans == 'No' or user_ans == 'NO' or user_ans == 'n'):
            break
    elif (user_ans == '2' or user_ans == 'yes' or user_ans == 'Yes' or user_ans == 'YES' or user_ans == 'y'):
            continue
    else:
        print("\nIncorrect input. The program will restart.\n")
        print(welcome_message)
        continue
   
print("\nThank you for using my program. The program will now close.")
close = True
