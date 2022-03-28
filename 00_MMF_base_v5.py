"""Added 03_get_age_v4
"""

# import statements

# functions


# check that the ticket name is not blank
def not_blank(question):
    while True:
        response = input(question).title()
        if not response.isalpha():  # Ensures input contains at least 1 letter
            print("Please enter a valid name")  # error if not
        else:
            return response     # otherwise, return the input


# check for valid integer (eg for age)
def integer_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer"
                  " (ie a whole number with no decimals)")


# -----main routine-----

# set up dictionaries/lists needed to hold data

# ask user if they had used the program before
# show instructions if necessary

# loop to get ticket details
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nYou have {MAX_TICKETS - count} seats left")
    else:
        # warns the user there is only one seat left
        print("\nYou have ONLY ONE seat left!")
    # get details
    name = not_blank("Whats your name? ")
    if name == "Xxx":
        break
    else:
        MIN_AGE = 12
        MAX_AGE = 110
        age = integer_checker("\nPlease enter the age of the ticket holder: ")
        if age < MIN_AGE:
            print(f"Sorry, {name} is too young for this movie")
        else:
            while MAX_AGE < age or MIN_AGE > age:
                if age >= MAX_AGE:
                    age = integer_checker(f"\nAt {age} {name} is very old. "
                                          f"Please re-enter {name}'s age: ")
                elif MIN_AGE > age:
                    print(f"Sorry, {name} is too young for this movie")
                    break
            if age >= MIN_AGE:
                count += 1  # don't want to include escape code in the count


if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still"
          f" {MAX_TICKETS - count} available")
else:
    print("\nYou have sold all the available tickets")

    # get name (cant be blank)

    # get age (between 12 and 130)

    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method

# calculate total sales and profit

# output data to text file
