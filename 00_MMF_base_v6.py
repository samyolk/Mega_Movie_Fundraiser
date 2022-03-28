"""Added 04_ticket_price_v4
Also includes total profit calculation in main routine.
Have changed variable 'count' to 'ticket_count' and made my formatting and
language in the print statements easier to understand
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


# -----main routine-----

# set up dictionaries/lists needed to hold data

# ask user if they had used the program before
# show instructions if necessary

# loop to get ticket details
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
profit = 0

while name != "Xxx" and ticket_count != MAX_TICKETS:
    if MAX_TICKETS - ticket_count > 1:
        print(f"\nThere are {MAX_TICKETS - ticket_count} tickets left")
    else:
        # warns the user there is only one seat left
        print("\nThere is ONLY ONE ticket left!")
    # get details
    name = not_blank("Enter ticket holder's name: ")
    if name == "Xxx":
        break
    else:
        MIN_AGE = 12
        MAX_AGE = 110
        age = integer_checker(f"\nPlease enter {name}'s age: ")
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
                ticket_count += 1  # don't want to include escape code in count

                # calculate ticket price
                ticket_price = calculate_ticket_price(age)
                print(f"For {name}, the ticket price is ${ticket_price:,.2f}")
                profit += (ticket_price - TICKET_COST_PRICE)


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


print(f"Profit: ${profit:,.2f}")

    # get name (cant be blank)

    # get age (between 12 and 130)

    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method

# output data to text file
