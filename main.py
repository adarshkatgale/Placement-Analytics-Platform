from database import connection
from student_menu import student_menu
from company_menu import company_menu
from eligibility_menu import eligibility_checker_menu
from analytics_menu import analytic_menu
from util import clear_screen,pause,print_headline,valid_choice

while True:
    clear_screen()

    print_headline("Placement Analytics Platform")
    print("1. Student Management")
    print("2. Company Management")
    print("3. Eligibility Checker")
    print("4. Analytics Dashboard")
    print("5. Exit")

    choice= valid_choice(5)

    if choice == 1:
        student_menu()

    elif choice == 2:
        company_menu()

    elif choice == 3:
        eligibility_checker_menu()
        
    elif choice == 4:
        analytic_menu()
        pause()

    elif choice == 5:
        connection.close()
        print("Thank you for using Placement Analytics Platform!")
        break
