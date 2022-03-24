""" fourth iteration of the integer checking function
wanted to limit the possibility of getting a false age for children < 12
this meant creating upper and lower age limits as constants
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
MIN_AGE = 12
MAX_AGE = 110
age = integer_checker("\nPlease enter the age of the ticket holder: ")
if age < MIN_AGE:
    print("Sorry, you are too young for this movie")
else:
    while age >= MAX_AGE:
        age = integer_checker(f"\nPlease enter a valid age "
                              f"between {MIN_AGE} and {MAX_AGE}: ")

print(f"Age = {age}")
