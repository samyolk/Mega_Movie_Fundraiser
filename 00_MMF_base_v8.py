"""Added 06_string_validator_v6 to 00_MMF_base_v7
"""

# import statements
import re
import pandas


# functions


# This function splits snacks into quantity and snack name
# It has to be called before the snack (name) can be evaluated against the
# valid_snacks list
def split_order(choice):
    # Regular expression to test and find out if on item starts with a number
    number_regex = "^[1-9]"

    # If item has a number, separate the item into two: number and item
    if re.match(number_regex, choice):
        quantity_required = int(choice[0])
        snack_name = choice[1:]

    # If item has no number, assume number required is 1
    else:
        quantity_required = 1
        snack_name = choice

    # Need to remove white space from around snack
    snack_name = snack_name.strip()
    return quantity_required, snack_name


# Function takes the question and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


def collate_order():
    # valid snacks holds list of oft snacks. Each item is itself a list with
    # all the acceptable input options for each snack - full name, initials and
    # abbreviations, as well as a reference number
    valid_snacks = [["popcorn", "p", "corn", "(1"],
                    ["m&ms", "mms", "m", "mm", "(2"],
                    ["pita chips", "chips", "pc", "pita", "c", "(3"],
                    ["water", "w", "(4"], ["orange juice", "oj", "(5"],
                    ["x", "exit", "(6"]]

    # Valid options for any yes/no questions
    valid_yes_no = [["y", "yes"], ["n", "no"]]

    # The snack_order list records the complete order for a single user
    snack_order = []
    # Maximum number of any snack item which can be ordered
    max_number_of_snacks = 4
    # Assumption that every user will want to order snacks
    getting_snacks = True
    while getting_snacks:
        # Firstly, find out whether the user wants to order snacks
        snacks_required = ""
        while snacks_required != "N" and snacks_required != "Y":
            # Response is passed to the generic string checking function with
            # the list of valid yes/no responses as parameters
            check_snacks = input("Do you want snacks? (Y/N): ").lower()
            snacks_required = get_choice(check_snacks, valid_yes_no)

        if snacks_required == "N":  # but if they don't want any snacks
            getting_snacks = False  # break the while loop
            break

        else:
            # Otherwise, for each snack, the generic string checker is called
            # with the 'ask_for_snacks. question and the list of valid snacks
            # as parameters
            option = ""
            while option != "X":
                snack = input("What snack do you want - or 'x' to stop "
                              "ordering: ").lower()
                snack = split_order(snack)
                quantity = snack[0]
                if quantity > max_number_of_snacks:
                    snack = None
                    print("Sorry, the maximum number you can order is 4")
                else:
                    snack = snack[1]
                    option = get_choice(snack, valid_snacks)
                    if option == "X":
                        getting_snacks = False

                    elif option is not None:  # Filters out invalid choices
                        snack_order.append([quantity, option])
    return snack_order


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


        # get snacks
        snack_order = collate_order()
        # print(snack_order)

        # After the loop is broken, check for an empty list
        if len(snack_order) > 0:   # If there is something in the list, print each item
            print("\nThis is a summary of your order:")
            for item in snack_order:
                print(f"\t{item[0]} \t{item[1]}")
        else:   # Otherwise, print this
            print("No snacks were ordered")


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
