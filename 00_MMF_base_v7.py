"""Moved the check of soles against maximum tickets into it's own function
Added lists to hold ticket holder's name and the price paid for their ticket
Added a dictionary to get data from these 2 new lists Added code to append name
and ticket price to the new lists (line 137 and 138) Added the import re and
import pandas libraries (installing pandas package if necessary)
Added the print statement for ticket profit on line 151 Modified the 'else'
statements under 'if MAX_TICKETS - ticket_count › 1:' (previously occupied
lines 158-160) to improve flow and readability Added the print details
(movie_frame: bottom 3 lines) which uses the pandas library to create a
printable DataFrame based on the dictionary
"""

# import statements
import re
import pandas
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


# calculate ticket price based on age
def calculate_ticket_price(ticket_holder_age):
    # ages - anything over standard_age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if ticket_holder_age in child_age:
        price = child_price
    elif ticket_holder_age in standard_age:
        price = standard_price
    else:
        price = retired_price
    return price


def check_max_tickets(maximum, sold):
    if maximum - sold > 1:
        print(f"There are {maximum - sold} tickets left")
    else:
        # warns user there is only one ticket left
        print("There is ONLY ONE ticket left!")


def check_valid_age(minimum, maximum):
    age = integer_checker(f"\nPlease enter {name}'s age: ")
    if age < MIN_AGE:
        print(f"Sorry, {name} is too young for this movie")
    else:
        while MAX_AGE < age or MIN_AGE > age:
            if age >= MAX_AGE:
                age = integer_checker(f"\nAt {age} {name} is very old. "
                                      f"Please re-enter {name}'s age: ")
    return age


# -----main routine-----

# set up dictionaries/lists needed to hold data
all_names = []
all_tickets = []


# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}


MIN_AGE = 12
MAX_AGE = 110
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
profit = 0


# ask user if they had used the program before
# show instructions if necessary

# loop to get ticket details
# initiate loop so it runs at least once

while name != "Xxx" and ticket_count != MAX_TICKETS:
    # check to make sure there are still tickets left
    check_max_tickets(MAX_TICKETS, ticket_count)

    # get details
    # get name
    name = not_blank("Enter ticket holder's name: ")
    if name == "Xxx":
        break
    else:
        age = integer_checker(f"\nPlease enter {name}'s age: ")
        if not age:
            continue
        else:
            ticket_count += 1

        # calculate ticket price
        ticket_price = calculate_ticket_price(age)
        print(f"For {name}, the ticket price is ${ticket_price:,.2f}")
        profit += (ticket_price - TICKET_COST_PRICE)

        # Add name and ticket price to lists
        all_names.append(name)
        all_tickets.append(ticket_price)


# calculate total sales and profit
if ticket_count < MAX_TICKETS:
    if ticket_count > 1:
        print(f"\n{ticket_count} tickets has been sold")
    else:
        print("\n1 ticket has been sold")
    if MAX_TICKETS - ticket_count > 1:
        print(f"{MAX_TICKETS - ticket_count} tickets are still available\n")
    else:
        print("1 ticket is still available\n")
else:
    print("\nAll the available tickets has been sold out!")

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)
print(f"Profit: ${profit:,.2f}")

    # get name (cant be blank)

    # get age (between 12 and 130)

    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method

# output data to text file
