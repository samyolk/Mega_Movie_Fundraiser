"""calculate price based on age
set up loop to run tests - according to test plan
assumes this function will be run in conjunction with integer checking and
valid age components
"""


def calculate_ticket_price(age):
    # ages - anything over standard_age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if age in child_age:
        ticket_price = child_price
    elif age in standard_age:
        ticket_price = standard_price
    else:
        ticket_price = retired_price
    return ticket_price


# main routine
# loop for testing purposes
test_cases = [["Jad", 15], ["Dan", 16], ["Jam", 64], ["Con", 65]]

for test in test_cases:
    test_name = test[0]
    test_age = test[1]
    print(f"The price is ${calculate_ticket_price(test_age):,.2f}")
