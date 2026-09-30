from company import CompanyManagement
from util import clear_screen,print_headline,pause, valid_choice
from database import connection

def company_menu():

    company_management= CompanyManagement(connection)
    while True:
        clear_screen()

        print_headline("Company Management")
        print("1. Add Company")
        print("2. View Companies")
        print("3. Update Company")
        print("4. Delete Company")
        print("5. Back")

        choice= valid_choice(5)
        if choice == 1:
            company_management.insert_company()
            pause()

        elif choice == 2:
            company_management.view_companies()
            pause()

        elif choice == 3:
            company_management.update_company()
            pause()

        elif choice == 4:
            company_management.delete_company()
            pause()

        elif choice == 5:
            break