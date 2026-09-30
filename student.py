from database import connection
from util import pause,valid_choice,get_valid_branch,get_valid_email,get_valid_name,get_valid_percentage,valid_graduation_year,valid_backlogs,valid_cgpa,valid_roll_no

class Student:

    def __init__(self, roll_no, name, email, branch,tenth_percentage,
                 twelfth_percentage, cgpa, active_backlogs, graduation_year):
        self.roll_no= roll_no
        self.name= name
        self.email= email
        self.branch= branch
        self.tenth_percentage= tenth_percentage
        self.twelfth_percentage= twelfth_percentage
        self.cgpa= cgpa
        self.active_backlogs= active_backlogs
        self.graduation_year= graduation_year
        

class StudentManagement:

    def __init__(self, connection):
        self.connection= connection
        self.cursor= connection.cursor()

    def insert_student(self):

        roll_no= valid_roll_no()
        if roll_no is None:
            return
        
        name= get_valid_name("Your")
        email= get_valid_email()
        branch= get_valid_branch()
        tenth_percentage= get_valid_percentage("Tenth Percentage")
        twelfth_percentage= get_valid_percentage("Twelfth Percentage")
        cgpa= valid_cgpa()
        active_backlogs= valid_backlogs()
        graduation_year= valid_graduation_year()

        student= Student(roll_no, name, email, branch, tenth_percentage, twelfth_percentage,
                         cgpa, active_backlogs, graduation_year)

        self.cursor.execute("""
        INSERT INTO Students
        (Roll_no ,Name, Email, Branch, Tenth_percentage,
        Twelfth_percentage, cgpa, Active_backlogs, Graduation_year)
        VALUES (?,?,?,?,?,?,?,?,?)
        """ , (student.roll_no, student.name, student.email, student.branch, student.tenth_percentage,
        student.twelfth_percentage, student.cgpa, student.active_backlogs, student.graduation_year))
        print("New student is added successfully.")
        self.connection.commit()

    def view_students(self):
        self.cursor.execute(" SELECT * FROM Students")
        rows= self.cursor.fetchall()

        if len(rows)== 0:
            print("No students records found.")
        else:
            for row in rows:
                student= Student(*row[1:])
                print(
                    f"Roll No: {student.roll_no},"
                    f"Name: {student.name}, "
                    f"Email: {student.email}, "
                    f"Branch: {student.branch}, "
                    f"!0th %: {student.tenth_percentage}, "
                    f"12th %: {student.twelfth_percentage}, "
                    f"CGPA: {student.cgpa}, "
                    f"Backlogs : {student.active_backlogs}, "
                    f"Graduation Year: {student.graduation_year}")

    def update_field(self,column_name, new_value, roll_no):
        self.cursor.execute(f"""
        UPDATE Students
        SET {column_name}= ?
        WHERE Roll_no= ?""",
        (new_value,roll_no))
        self.connection.commit()

        if self.cursor.rowcount == 0:
            print("Student not found")
        else:
            print(f"{column_name} Updated successfully")

    def update_student(self):

        roll_no= valid_roll_no()
        if roll_no is None:
            return

        print("Update student details.")
        print("===========================")
        print("1. Name")
        print("2. Email")
        print("3. CGPA")
        print("4. Active Backlogs")
        print("5. Graduation Year")
        print("===========================")
        choice= valid_choice(5)

        if choice== 1:
            new_name= get_valid_name("your")
            self.update_field("Name", new_name, roll_no)

        elif choice == 2:
            new_email= get_valid_email()
            self.update_field("Email", new_email,roll_no)

        elif choice== 3:

            new_cgpa= valid_cgpa()
            self.update_field("CGPA",new_cgpa, roll_no)

        elif choice== 4:

                active_backlogs= valid_backlogs()
                self.update_field("Active_backlogs", active_backlogs,roll_no)
        elif choice== 5:
        
                graduation_year= valid_graduation_year()
                self.update_field("Graduation_year", graduation_year, roll_no)

        else:
            print("Please try again")

    def delete_student(self):
        roll_no= valid_roll_no()
        if roll_no is None:
            return 

        self.cursor.execute("""
        DELETE FROM students
        WHERE Roll_no= ?""",
        (roll_no,))
        self.connection.commit()

        if self.cursor.rowcount ==1:
            print("Student is deleted successfully.")
        else:
            print("Student not found.")

