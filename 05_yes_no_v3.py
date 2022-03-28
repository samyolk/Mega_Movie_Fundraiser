"""Includes testing loop
This component, originally designed to ask if the user wants to purchase
snacks, asks for a Yes/No response and keeps asking - for the purposes of
testing. In this version the program makes a decision based on the first
letters of response
"""


def yes_or_no_response(question):
    error_message = "Please answer 'Y' or 'N'"
    valid_responses = ["y", "yes", "n", "no"]
    response = input(question).lower()
    while response not in valid_responses:
        print(error_message)
        response = input(question).lower()

    if response == "n" or response == "no":
        return False
    else:
        return True


# main routine
# temporary input statements - during development
testing = True
while testing:
    snacks_required = yes_or_no_response("Do you want snacks? ")
    if not snacks_required:
        print("Valid answer. You don't want snacks")
    else:
        print("Valid answer. You want snacks")
    print()
