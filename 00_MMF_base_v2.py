"""Added 01_check_name_v3 to original v1 of this base code
"""

# import statements

# functions

# check that the ticket name is not blank
def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():  # Ensures input contains at least 1 letter
            print("You can't leave this blank...")  # error if not
        else:
            return response     # otherwise, return the input


# -----main routine-----

# set up dictionaries/lists needed to hold data

# ask user if they had used the program before
# show instructions if necessary

# loop to get ticket details

    # get name (cant be blank)
    name = not_blank("What's your name? ")
    # get age (between 12 and 130)

    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method

# calculate total sales and profit

# output data to text file
