import random
if __name__ == '__main__':
    # Variables:
    lowercase_alphabet_yes_or_no = ""
    uppercase_alphabet_yes_or_no = ""
    password_length = 0
    lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    user_generated_password = ""
    number_range = 0
    user_possabilities = ""

    # --------------------------------------------------------------------------------------------------------
    # User Input Questions:

    while password_length <= 0:
        try:
            password_length = int(input(
                "How long would you like your password to be?: "))
        except ValueError:
            print("Please enter a number greater than 0")

    while lowercase_alphabet_yes_or_no != 'y' and lowercase_alphabet_yes_or_no != 'n':
        lowercase_alphabet_yes_or_no = input(
            "Do you want to use lowercase letters: 'Y' or 'N' ").lower()
        print("Please select 'Y' or 'N' for the question below to continue: ")

    while uppercase_alphabet_yes_or_no != 'y' and uppercase_alphabet_yes_or_no != 'n':
        uppercase_alphabet_yes_or_no = input(
            "Do you want to use uppercase letters: 'Y' or 'N'").lower()
        print("Please select 'Y' or 'N' for the question below to continue: ")

    # --------------------------------------------------------------------------------------
    # Taking user input and updating For Loop in next section:

    if uppercase_alphabet_yes_or_no == 'y' and lowercase_alphabet_yes_or_no == 'n':
        user_possabilities = uppercase_alphabet
        number_range = 25
    if lowercase_alphabet_yes_or_no == 'y' and uppercase_alphabet_yes_or_no == 'n':
        user_possabilities = lowercase_alphabet
        number_range = 25
    if lowercase_alphabet_yes_or_no == 'y' and uppercase_alphabet_yes_or_no == 'y':
        user_possabilities = lowercase_alphabet + uppercase_alphabet
        number_range = 51
    if lowercase_alphabet_yes_or_no == 'n' and uppercase_alphabet_yes_or_no == 'n':
        print("Please select one of the above options:")

    # --------------------------------------------------------------------------------------
    # Loop for generating userpassword

    for x in range(0, password_length):
        a = random.randint(0, number_range)
        user_generated_password = user_generated_password + \
            user_possabilities[a]

    print(f"Here is your generated Password: {user_generated_password}")

    # --------------------------------------------------------------------------------------

    ''' 
To-Do:
    - Add numbers/Symbols
    - Give the ability to generate a new password with the saved user settings
    - Give the ability to generate more then one password.
    - Look into while loops to replace the userprompts
    - Consider using functions for the user 'input question' section.
    -Look into 'Match' statements to make the 'Taking user input and updating For Loop in next section:' 
     More efficient 
        - https://www.pythonpool.com/match-case-python/
    - Dictionaries for lowercase_alphabet_yes_or_no, etc..
    - use string library to do away with variables containing alphabet characters. 
        - https://docs.python.org/3/library/string.html

    
Completed:
    - Use Snake case(Styling)(pep8)
    - Add more validation of the user input
    '''
