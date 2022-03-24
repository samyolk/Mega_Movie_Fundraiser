""" integer checking function - loops until a valid number is entered
this version uses 'isinstance()' to validate the integer and cuts down on the
number of parameters required in the function by incorporating the valid age
range into a loop in the main routine
"""


def integer_checker(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("\nPlease enter an integer"
                  " (ie a whole number with no decimals)")


# main routine
# check for valid age - must be between 120 and 110
age = integer_checker("\nPlease enter the age of the ticket holder: ")
while not 12 <= age <= 110:
    age = integer_checker("\nPlease enter and integer between 12 and 110: ")
print(f"Age = {age}")
