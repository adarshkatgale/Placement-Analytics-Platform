from analytics import placement_overview, company_wise_analysis
from util import clear_screen, print_headline, pause, valid_choice
from database import connection

def analytic_menu():
    while True:

        clear_screen()

        print_headline("Placement Analysis")
        print("1. Placement overview")
        print("2. Company wise analysis.")
        print("3. Back")

        choice= valid_choice(3)

        if choice== 1:
            placement_overview()
            pause()

        elif choice== 2:
            company_wise_analysis()
            pause()

        elif choice== 3:
            break

        else:
            print("Please try again..")