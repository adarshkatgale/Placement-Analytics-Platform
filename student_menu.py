from student import StudentManagement
from util import clear_screen,pause,print_headline,valid_choice
from database import connection
def student_menu():
    student_management= StudentManagement(connection)
    while True:
        clear_screen()

        print_headline("Student Management")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back")

        choice= valid_choice(5)

        if choice== 1:
            student_management.insert_student()
            pause()

        elif choice== 2:
            student_management.view_students()
            pause()

        elif choice== 3:
            student_management.update_student()
            pause()

        elif choice== 4:
            student_management.delete_student()
            pause()

        elif choice== 5:
            break
