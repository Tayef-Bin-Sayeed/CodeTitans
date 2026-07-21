while True:
    pass_ = input("Enter a sample password: ")

    if " " in pass_:
        print("Password contains spaces. Try again!")
        continue

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

    if len(pass_) <= 8 and points <= 8:
        print("Simple Password")
    elif points < 12:
        print("Moderate Password")
    else:
        print("Strong Password")

    choice = input("Do you want to check another password? (If no, then press N/n): ")

    if choice == "n":
        print("Goodbye!")
        break
    elif choice == "N":
        print("Goodbye!")
        break

#Tayef(L) : Wrote the space input response
#Mohim: Wrote point calculation
#Soumyajit: Wrote Password Strength Determination
#Mukto: Wrote the exit code
#Mridu: Put the code in a while loop
