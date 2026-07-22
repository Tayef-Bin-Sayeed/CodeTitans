#CodeTitans

#Mridu's Part
while True:
    pass_ = input("Enter a sample password: ")
# The code is put in a while loop so differnets passwords and their strength can be determined multiple times.
#--------------------------------------------------------------
#Tayef's Part
    if " " in pass_:
        print("Password contains spaces. Try again!")
        continue
# If the password contains a space, it's handled as a error and the loop starts again.
#----------------------------------------------------------------
#Mohim's Part
    letters = 0
    numbers = 0
    special = 0

    for char in pass_:
        if char.isalpha():
            letters += 2
        elif char.isdigit():
            numbers += 1
        else:
            special += 2

    points = letters + numbers + special
# Points are given to the password on how many numbers,alphabets and special characters are used in the password.
#-----------------------------------------------------------------
#Soumyajit's Part
    if len(pass_) <= 8 and points <= 8:
        print("Simple Password")
    elif points < 12:
        print("Moderate Password")
    else:
        print("Strong Password")
# Based on the length and points, the strength of the password is determined.
#--------------------------------------------------------------------
#Mukto's Part
    choice = input("Do you want to check another password? (If no, then press N/n): ")

    if choice == "n":
        print("Goodbye!")
        break
    elif choice == "N":
        print("Goodbye!")
        break
# Here, the input choice N or n breaks the loop.
#------------------------------------------------------------------------------

#Members and what they have wrote:
#Tayef(L) : Wrote the space input response
#Mohim: Wrote point calculation
#Soumyajit: Wrote Password Strength Determination
#Mukto: Wrote the exit code
#Mridu: Put the code in a while loop
