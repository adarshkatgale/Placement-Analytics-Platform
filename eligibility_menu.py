from util import pause, print_headline, clear_screen, valid_choice
from eligibility import company_eligibility_checker, student_eligibility_checker

def eligibility_checker_menu():

    while True:
        clear_screen()

        print_headline("Eligibility Checker")
        print("1. Company wise Eligibility")
        print("2. Student wise Eligibility")
        print("3. Back")

        choice= valid_choice(3)

        if choice == 1:
            company_eligibility_checker()
            pause()

        elif choice == 2:
            student_eligibility_checker()
            pause()

        elif choice == 3:
            break
        else:
            print("Invalid choice! Please try again")
            pause()