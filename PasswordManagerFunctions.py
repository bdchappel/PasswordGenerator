import csv
import os


def menu_call():
    user_selection = ""
    while user_selection not in range(1, 4):
        print("Please chose an option from the menu below:")
        print("1: Generate a Password | 2: Create Entry | 3: Edit Entry | 4: Delete Entry.")
        user_selection = int(input(">:"))
    return user_selection


def create_entry():
    user_answer = ""
    while user_answer != 'y':
        entry_user_website_url = input(
            "Please enter the website this is for: ")
        entry_user_name = input(
            "Please enter the username you would like to store: ")
        entry_user_password = input(
            "Please enter the password you would like to store: ")
        print(
            f"Does the following information look correct? website: {entry_user_website_url} Username:{entry_user_name} password: {entry_user_password}")
        user_answer = input(
            "Please type 'Y' for yes, or any key to redo continue: ")
    with open(os.path.dirname(__file__) + "\\" + "PasswordManagerUserFile.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(entry_user_website_url +
                           entry_user_name + entry_user_password)
    print(os.path.dirname(__file__) + 'PasswordManagerUserFile.csv')
