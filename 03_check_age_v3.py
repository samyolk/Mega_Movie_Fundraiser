""" third iteration of the integer checking function
simplified try/except and created AGE_RANGE as a constant
"""


def integer_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer"
                  " (ie a whole number with no decimals)")


# main routine
# check for valid age
AGE_RANGE = range(12, 110)  # between 12 and 110 inclusive
age = integer_checker("\nPlease enter the age of the ticket holder: ")
while age not in AGE_RANGE:    # must be between 120 and 110
    age = integer_checker("\nPlease enter and integer between 12 and 110: ")

print(f"Age = {age}")
