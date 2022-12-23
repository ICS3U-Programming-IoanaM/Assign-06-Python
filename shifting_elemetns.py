#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Dec. 23, 2022
# shifts the elements in a list x times in a specified direction


def shift_list(nums_list, shifts):
    # variables
    list_length = len(nums_list) - 1

    for counter in range(shifts):
        previous_element = nums_list[list_length]
        nums_list.pop(list_length)
        nums_list.insert(0, previous_element)

    return nums_list


# function to display what the program is about and how to use it 
def opening_message():
    print()
    print("Hello and thank you for using this program!")
    print("In this program, you will be entering numbers to add into a list, then the")
    print("elements (numbers) will shift to the left x amount of times.")
    print("Example:")
    print("Enter a number (q to quit): 3")
    print("Enter a number (q to quit): 2")
    print("Enter a number (q to quit): 1")
    print("Enter a number (q to quit): q")
    print("Here is your list: [3, 2, 1]")
    print("How many elements to the left do you want to shift this list? 2")
    print("Your list shifted 2 elements to the left is [2, 1, 3]")
    print()
    print()


# main gets user input and runs all the other functions
def main():
    # variables
    list_of_int = []
    final_list = []

    # opening message
    opening_message()

    # getting user input for each number
    while(True):
        user_num_str = input("Enter a number you want in your list (q to quit): ")

        # user doesn't want to enter more numbers
        if (user_num_str == "q" or user_num_str == "Q"):
            break

        # exception handling
        try:
            user_num_int = int(user_num_str)

        # user input is not an integer
        except Exception:
            print("Please make sure your input is an integer!")

        # use input is an integer
        else:
            # adds user input to the list
            list_of_int.append(user_num_int)

    print(f"Here is your list: {list_of_int}")

    # gets user input for how many elements to the left the user wants to shift to the left
    shifted_elements_str = input("How many elements do you want to shift to the left? ")

    # exception handling for second set of input
    try:
        shifted_elements_int = int(shifted_elements_str)

    # user input is not an integer
    except Exception:
        print("Please make sure your input is an integer!")

    # user input is valid
    else:
        # calls function to shit the elements of the list
        final_list = shift_list(list_of_int, shifted_elements_int)

        # final message
        print(f"The list shifted {shifted_elements_int} elements to the left is {final_list}")


# runs main
if __name__ == "__main__":
    main()
