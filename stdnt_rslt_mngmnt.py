# CodeTitans - Student Result Management System


print("Welcome to the Student Result Management System!")

students = []  # List for storing student dictionaries
total_students = 0

# Grade calculator
def calculate_grade(marks):
    if marks >= 80:
        return "A+"
    elif marks >= 70:
        return "A"
    elif marks >= 60:
        return "A-"
    elif marks >= 50:
        return "B"
    elif marks >= 45:
        return "C"
    elif marks >= 35:
        return "D"
    else:
        return "F"

# Add student function which asks for required info and appends it to the dictionary
def add_student():
    global total_students

    print("\n------Add Student------\n")
    try:
        name = (input("Enter student name: " )).upper()
        math = float(input("Math marks: " ))
        sci  = float(input("Science marks: " ))
        bgs  = float(input("BGS marks: " ))
        rel  = float(input("Religion marks: " ))
        ict  = float(input("ICT marks: " ))
        eng1 = float(input("English 1st paper: "))
        eng2 = float(input("English 2nd paper: "))
        ban1 = float(input("Bangla 1st paper: " ))
        ban2 = float(input("Bangla 2nd paper: " ))
    except ValueError:
        print("Invalid marks entered. Please enter valid numbers.")
        add_student()
        return

    all_marks = [math, sci, bgs, rel, ict, eng1, eng2, ban1, ban2]

    for m in all_marks:
        if m < 0 or m > 100:
            print("Invalid marks entered. Please enter marks between 0 and 100.")
            add_student()
            return

    total_marks = sum(all_marks)
    average = round((total_marks / 9), 2)

    failed = False
    for m in all_marks:
        if m < 45:
            failed = True

    grade = "F" if failed else calculate_grade(average)

    student = {
        "name"   : name,
        "math"   : math,
        "sci"    : sci,
        "bgs"    : bgs,
        "rel"    : rel,
        "ict"    : ict,
        "eng"    : eng1,
        "eng2"   : eng2,
        "ban"    : ban1,
        "ban2"   : ban2,
        "total"  : total_marks,
        "average": average,
        "grade"  : grade,
        "failed" : failed}

    students.append(student)
    total_students += 1

    if failed:
        print(f"{name} added. Result: FAIL. Overall GPA: 0. Class Position: N/A")
    else:
        print(f"{name} added. Grade: {grade}")

# Function to return to main menu
def ask_user():
    ask = input("\nPress any key to return to main menu:  ")
    return

# Prints report card of a student
def generate_report():
    if total_students == 0:
        print("\nNo students added yet.")
        return

    name = input("Enter student name to see report: ")
    found = False

    for student in students:
        if student["name"].upper() == name.upper():
            found = True
            print("\n------REPORT CARD------\n")
            print("Name:"       , student["name"])
            print("Math:"       , student["math"] , "; Grade:", calculate_grade(student["math"]))
            print("Science:"    , student["sci"]  , "; Grade:",calculate_grade(student["sci" ]))
            print("BGS:"        , student["bgs"]  , "; Grade:",calculate_grade(student["bgs" ]))
            print("Religion:"   , student["rel"]  , "; Grade:",calculate_grade(student["rel" ]))
            print("ICT:"        , student["ict"]  , "; Grade:",calculate_grade(student["ict" ]))
            print("English:"    , student["eng"]  , "; Grade:",calculate_grade(student["eng" ]))
            print("English 2nd:", student["eng2"] , "; Grade:",calculate_grade(student["eng2"]))
            print("Bangla:"     , student["ban"]  , "; Grade:",calculate_grade(student["ban" ]))
            print("Bangla 2nd:" , student["ban2"] , "; Grade:",calculate_grade(student["ban2"]))
            print("Total:"      , student["total"], "/ 900")
            print("Average:"    , student["average"])
            print("Grade:"      , student["grade"])
            print("------------------------")
            break

    if found == False:
        print("Student not found.")

    ask_user()

# Shows class ranking of sudents (Highest average first)
def class_ranking():
    if total_students == 0:
        print("\nNo students added yet.")
        return

    # Only rank students who passed
    passed_students = []
    for student in students:
        if not student["failed"]:
            passed_students.append(student)

    for i in range(len(passed_students)):
        for j in range(len(passed_students) - 1 - i):
            if passed_students[j]["average"] < passed_students[j + 1]["average"]:
                temp = passed_students[j]
                passed_students[j] = passed_students[j + 1]
                passed_students[j + 1] = temp

    print("\n----CLASS-RANKING----\n")
    rank = 1
    for student in passed_students:
        print(f"\n{rank}. {student['name']} \nAverage: {student['average']} \nGrade: {student['grade']}")
        rank += 1

    if len(passed_students) == 0:
        print("No one passed yet.")

# main menu loop
def menu_screen():
    while True:
        print("\n--------Student Result Management System--------\n\n1. Add Student\n2. Generate Report Card\n3. Class Ranking\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            generate_report()
        elif choice == "3":
            class_ranking()
        elif choice == "4":
            print("Thanks for using the program.")
            break
        else:
            print("Wrong choice, try again.")

menu_screen()