should_continue = True

while should_continue:
    user_input = input("Enter the marks or type 'stop' to quit the program: ")

    if user_input.lower() == "stop":
        print("Exiting program.")
        should_continue = False
    else:
        try:
            grade_input = int(user_input)
            if 0 <= grade_input <= 100:
                if 90 <= grade_input <= 100:
                    grade = "A"
                elif 87 <= grade_input < 90:
                    grade = "A-"
                elif 84 <= grade_input < 87:
                    grade = "B+"
                elif 80 <= grade_input < 84:
                    grade = "B"
                elif 77 <= grade_input < 80:
                    grade = "B-"
                elif 74 <= grade_input < 77:
                    grade = "C+"
                elif 70 <= grade_input < 74:
                    grade = "C"
                elif 67 <= grade_input < 70:
                    grade = "C-"
                elif 64 <= grade_input < 67:
                    grade = "D+"
                elif 62 <= grade_input < 64:
                    grade = "D"
                elif 60 <= grade_input < 62:
                    grade = "D-"
                else:
                    grade = "F"

                print(f"The grade is: {grade}")
            else:
                print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
