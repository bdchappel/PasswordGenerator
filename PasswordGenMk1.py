import random
#Global variable
lowerCaseAlphabetYesorNo = ""
upperCaseAlphabetYesorNo = ""
PasswordLength = 0
lowerCaseAlphabet = 'abcdefghijklmnopqrstuvwxyz'
upperCaseAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
userGeneratedPassword = ""
rangeNumber = 0
userPossabilities = ""


#User input questions
def userInput():
    global lowerCaseAlphabetYesorNo 
    lowerCaseAlphabetYesorNo = input("Do you want to use lowercase letters 'y or n' ")
    global upperCaseAlphabetYesorNo 
    upperCaseAlphabetYesorNo = input("Do you want to use uppercase letters 'y or n' ")
    if lowerCaseAlphabetYesorNo == 'n' and upperCaseAlphabetYesorNo == 'n':
        print("Please select one of the following options with 'y' to continue.")
        userInput()


def PasswordLengthQuestion():
    global PasswordLength 
    PasswordLength = int(input("How long would you like your password to be?: "))
    if PasswordLength == 0:
        print("Please enter a number greater than 0")
        PasswordLengthQuestion()


userInput()
PasswordLengthQuestion()


if upperCaseAlphabetYesorNo == 'y' and lowerCaseAlphabetYesorNo == 'n':
    userPossabilities = upperCaseAlphabet
    rangeNumber = 25
if lowerCaseAlphabetYesorNo == 'y' and upperCaseAlphabetYesorNo == 'n':
    userPossabilities = lowerCaseAlphabet
    rangeNumber = 25
if lowerCaseAlphabetYesorNo == 'y' and upperCaseAlphabetYesorNo == 'y':
    userPossabilities = lowerCaseAlphabet + upperCaseAlphabet
    rangeNumber = 51
if lowerCaseAlphabetYesorNo == 'n' and upperCaseAlphabetYesorNo == 'n':
    print("Please select one of the above options:")


#Loop for above if statements to generate userpassword
print(rangeNumber)
for x in range(0, int(PasswordLength)):
    a = random.randint(0,rangeNumber)
    userGeneratedPassword = userGeneratedPassword + userPossabilities[a]


print(userGeneratedPassword)


''' 
     ****Goals****
 - Add numbers/Symbols
 - Give the ability to generate a new password with the saved user settings
 - Give the ability to generate more then one password.
 - Add more validation of the user input
 - Use Snake case(Styling)
 - Look into while loops to replace the userprompts
'''