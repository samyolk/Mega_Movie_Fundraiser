"""Based on 06_string_validator_v2, this program uses the string validator
function to ask if the user wants to order snacks, if the response is 'yes'
the function is called repeatedly to check that the choice of snacks is valid.
The user choice 'x' to stop ordering snacks.
"""


def get_choice(question, valid_choices):
    choice_error = "Sorry, that is not a valid choice"

    choice = input(question).lower()
    for item in valid_choices:
        if choice in item:
            choice = item[0].title()
            return choice

    print(choice_error)
    return get_choice(question, valid_choices)


# main routine
ask_for_snack = "What snack do you want? "
valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                ["pita chips", "chips", "pc", "pita", "c", "3"],
                ["water", "w", "4"]]

