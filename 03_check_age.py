# integer checking function - first trial method

def integer_checker(question, low_num, high_num):
    error = f"Please enter an integer between {low_num} and {high_num}"
    valid = False
    while not valid:
        # asking user for a number and check to see if its valid
        try:
            number_to_check = int(input(question))
            if low_num <= number_to_check <= high_num:
                return number_to_check
            else:
                print(error)
        except ValueError:
            print("\nPlease enter an integer"
                  " (ie a whole number with no decimals)")


# main routine
# check for valid age - must be between 120 and 110
age = integer_checker("\nPlease enter the age of the ticket holder: ", 12, 110)
print(f"Age = {age}")
