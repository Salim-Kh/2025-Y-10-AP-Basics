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
# Main Routine Goes Here
for item in range(0, 2):
    width = num_check("Width:" )
    print(width)

print()

for item in range(0, 2):
    height = num_check("height:" )
    print(height)