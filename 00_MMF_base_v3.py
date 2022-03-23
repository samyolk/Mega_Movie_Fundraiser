"""Added 02_ticket_loop_v4 to original v1 of this base code
"""

# import statements

# functions

# check that the ticket name is not blank


def not_blank(question):
    while True:
        response = input(question).title()
        if not response.isalpha():  # Ensures input contains at least 1 letter
            print("You can't leave this blank...")  # error if not
        else:
            return response     # otherwise, return the input


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
    if name != "Xxx":
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
