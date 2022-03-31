import random
import string
import pyperclip


def generate_new_password():
    password_length = 0
    while password_length <= 0:
        try:
            password_length = int(input(
                "How long would you like your password to be?: "))
        except ValueError:
            print("Please enter a number greater than 0 to continue")

    lowercase_alphabet_yes_or_no = user_input_questions("lowercase Letters")
    uppercase_alphabet_yes_or_no = user_input_questions("Uppercase Letters")
    numbers_yes_or_no = user_input_questions("Numbers")
    symbols_yes_or_no = user_input_questions("Symbols")

# --------------------------------------------------------------------------------------
# Taking user input and updating For Loop in next section:
    user_possabilities = ""

    if uppercase_alphabet_yes_or_no == 'y':
        user_possabilities += string.ascii_uppercase
    if lowercase_alphabet_yes_or_no == 'y':
        user_possabilities += string.ascii_lowercase
    if numbers_yes_or_no == 'y':
        user_possabilities += string.digits
    if symbols_yes_or_no == 'y':
        user_possabilities += string.punctuation

# --------------------------------------------------------------------------------------
    user_password_satisfaction = ""
    user_generated_password = generate_user_pass(
        user_possabilities, password_length)
    print("")
    print(f"Here is your generated Password: {user_generated_password}")
    pyperclip.copy(user_generated_password)


def generate_user_pass(user_possabilities, password_length):
    user_generated_password = ""
    number_range = 0
    number_range = len(user_possabilities) - 1

    for x in range(0, password_length):
        a = random.randint(0, number_range)
        user_generated_password += user_possabilities[a]
    return user_generated_password


def user_input_questions(user_question):
    user_answer = ""
    while user_answer != 'y' and user_answer != 'n':
        print("Please type 'Y' for yes or 'N' for no for the question below to continue: ")
        user_answer = input(
            f"Would you like {user_question} in your password? 'Y' or 'N' ").lower()
    return user_answer


# --------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # --------------------------------------------------------------------------------------------------------
    # User Input Questions:
    """
    password_length = 0
    while password_length <= 0:
        try:
            password_length = int(input(
                "How long would you like your password to be?: "))
        except ValueError:
            print("Please enter a number greater than 0 to continue")

    lowercase_alphabet_yes_or_no = user_input_questions("lowercase Letters")
    uppercase_alphabet_yes_or_no = user_input_questions("Uppercase Letters")
    numbers_yes_or_no = user_input_questions("Numbers")
    symbols_yes_or_no = user_input_questions("Symbols")

# --------------------------------------------------------------------------------------
# Taking user input and updating For Loop in next section:
    user_possabilities = ""

    if uppercase_alphabet_yes_or_no == 'y':
        user_possabilities += string.ascii_uppercase
    if lowercase_alphabet_yes_or_no == 'y':
        user_possabilities += string.ascii_lowercase
    if numbers_yes_or_no == 'y':
        user_possabilities += string.digits
    if symbols_yes_or_no == 'y':
        user_possabilities += string.punctuation

# --------------------------------------------------------------------------------------
    user_password_satisfaction = ""
    user_generated_password = generate_user_pass(
        user_possabilities, password_length)
    print("")
    print(f"Here is your generated Password: {user_generated_password}")
    pyperclip.copy(user_generated_password)


    #Loop to constantly prompt the user to generate a new password with saved settings.
    while user_password_satisfaction != 'n':
        user_password_satisfaction = input(
            "Would you like to generate a new password with your saved settings? 'Y' for yes or 'N' for no: ").lower()
        user_generated_password = generate_user_pass(
            user_possabilities, password_length)
        print("")
        print(f"Here is your generated Password: {user_generated_password}")
        pyperclip.copy(user_generated_password)
    """
# --------------------------------------------------------------------------------------

    ''' 
    To-Do:
    -Classes
    -Functions


        - Give the ability to generate more then one password.
        - Dictionaries for lowercase_alphabet_yes_or_no, etc..
        - use string library to do away with variables containing alphabet/numbers/symbols. 
            - https://docs.python.org/3/library/string.html

        
    Completed:
        - add password to clipboard
        - Give the ability to generate a new password with the saved user settings
        - Use Snake case(Styling)(pep8)
        - Add more validation of the user input
            - Look into while loops to replace the userprompts
            - Consider using functions for the user 'input question' section.
        - Add numbers/Symbols
    '''
