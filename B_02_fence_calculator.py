# Ask user for width snf loop until they
# Enter a number that is more than zero
def num_check(question):

        error = "Please a number that is more than zero\n"
        while True:


            try:
                # ask the user for a number
                    response = float(input(question))

                # check that the number is more than zero

                    if response >0:
                       return response
                    else:
                        print(error)


            except ValueError :
                print(error)


# Main routine starts here...

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width:")
    height = num_check("height:")
    cost = num_check("cost/m:")

    # calculate perimeter and price for the fence
    perimeter = 2 * (width + height)
    price = perimeter * cost

    # Display output
    print()
    print(f"perimeter: {perimeter} units")
    print(f"price: ${price: .2f}")
    # Ask the user if they want to do another calculation
    keep_going = input("press enter to loop, or any key to quit.  ")
    print()

print("Thank you for using the area / fence calculator")
