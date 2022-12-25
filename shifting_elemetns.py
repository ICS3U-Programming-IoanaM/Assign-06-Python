#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Dec. 23, 2022
# shifts the elements in a list x times in a specified direction


def rerun():
    print()
    while True:
        # asks user if they want to rerun the program
        play_again = input("Do you want to rerun the program? (y/n) ")

        if play_again == "y" or play_again == "Y":
            return True

        if play_again == "n" or play_again == "N":
            return False

        print("Please type either y or n.")


# function that shifts the elements of the list to the right
def shift_left(user_list, shifts):
    # actually shifts the elements
    for counter in range(shifts):
        first_element = user_list[0]
        user_list.pop(0)
        user_list.append(first_element)

    return user_list


# function that shifts the elements of the list to the left
def shift_right(user_list, shifts):
    # variables
    list_length = len(user_list) - 1

    # actually shifts the elements
    for counter in range(shifts):
        previous_element = user_list[list_length]
        user_list.pop(list_length)
        user_list.insert(0, previous_element)

    return user_list


# function to display what the program is about and how to use it
def opening_message():
    print()
    print("Hello and thank you for using this program!")
    print("In this program, you will be entering values to add into a list, then the")
    print("elements (the values) will shift to the left x amount of times.")
    print("Example:")
    print("Enter a number (/q to quit): 3")
    print("Enter a number (/q to quit): abc")
    print("Enter a number (/q to quit): 1.1")
    print("Enter a number (/q to quit): q")
    print("Here is your list: [3, abc, 1.1]")
    print("How many elements to the left do you want to shift this list? 2")
    print("Your list shifted 2 elements to the left is [abc, 1.1, 3]")
    print()
    print()


# main gets user input and runs all the other functions
def main():
    # variables
    go_again = True

    # opening message
    opening_message()

    while go_again:
        # lists
        list_of_inputs = []
        final_list = []

        # getting user input for each number
        while True:
            user_input = input("Enter a number you want in your list (/q to quit): ")

            # user doesn't want to enter more numbers
            if user_input == "/q":
                break

            # adds input to list
            list_of_inputs.append(user_input)

        # displays the list
        print(f"Here is your list: {list_of_inputs}")

        # gets user input for how many elements to the left the user wants to shift to the left
        shifted_elements_str = input("How many elements do you want to shift? ")

        # exception handling for second set of input
        try:
            shifted_elements_int = int(shifted_elements_str)

        # user input is not an integer
        except Exception:
            print("Please make sure your input is an integer!")
            go_again = rerun()

        # user input is valid
        else:
            # user input is negative
            if shifted_elements_int < 0:
                print(
                    f"You can't shift a list {shifted_elements_int} times! Please enter a positive integer!"
                )

            # user input is whole
            else:
                while True:
                    # asks which direction the user wants to shift elements to
                    direction = input(
                        "which way do you want to shift the elements (l for left r for right)? "
                    )

                    if direction == "l":
                        # calls function to shift to the left
                        final_list = shift_left(list_of_inputs, shifted_elements_int)
                        break

                    elif direction == "r":
                        # call function to shift to the right
                        final_list = shift_right(list_of_inputs, shifted_elements_int)
                        break

                    print("Please enter either l or r.")

                # final message
                print(
                    f"The list shifted {shifted_elements_int} elements to the left is {final_list}"
                )
            go_again = rerun()


# runs main
if __name__ == "__main__":
    main()
