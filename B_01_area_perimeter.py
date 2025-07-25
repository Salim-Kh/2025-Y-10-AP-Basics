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

    # calculate area/ perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"perimeter: {perimeter} units")
    print(f"Area: {area} square units")
    # Ask the user if they want to keep going
    keep_going = input("press enter to keep going or any key to quit.  ")
    print()

print("Thank you for using the area / perimeter calculator")
