from PasswordManagerFunctions import menu_call, create_entry
from PasswordGenerator import generate_new_password


def process_menu_choice(menu_choice):
    match menu_choice:
        case 1:
            generate_new_password()
        case 2:
            create_entry()
        case 3:
            return 0   # 0 is the default case if x is not found
        case 4:
            return 3


if __name__ == '__main__':
    menu_choice = menu_call()
    process_menu_choice(menu_choice)
