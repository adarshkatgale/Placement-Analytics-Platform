from database import cursor
from eligibility import get_company_eligible_students
from util import print_headline


def placement_overview():

    cursor.execute("SELECT COUNT(*) FROM Students")
    total_students= cursor.fetchone()[0]

    print(f"Total students: {total_students}")

    cursor.execute(" SELECT COUNT(*) FROM Companies")
    total_companies= cursor.fetchone()[0]

    print(f'Toatal companies: {total_companies}')

    cursor.execute("SELECT AVG(CGPA) FROM Students")
    average_cgpa= cursor.fetchone()[0]
    if average_cgpa is None:
        print("No students found.")
    else:
        print(f"Average CGPA: {average_cgpa:.2f}")

    cursor.execute("""
    SELECT COUNT(*)
    FROM Students
    WHERE Active_backlogs = 0
    """)
    students_without_backlogs= cursor.fetchone()[0]
    print(f'Students with no backlogs: {students_without_backlogs}')

    cursor.execute("""
    SELECT COUNT(*)
    FROM Students
    WHERE Active_backlogs > 0
    """)
    students_with_backlogs= cursor.fetchone()[0]
    print(f"Students with active backlogs: {students_with_backlogs}")


def company_wise_analysis():

    print_headline("Company Wise Analysis")

    cursor.execute("SELECT COUNT(*) FROM Students")
    total_students= cursor.fetchone()[0]

    cursor.execute(" SELECT * FROM Companies")
    companies= cursor.fetchall()

    highest_company=None #high eligible students company
    highest_percentage=0 #highest percentage of eligible students for that company
    print(f"{'Company Name':<18}{'Total Students':<18}{'Eligible Students':<20}{'Eligibility Percentage':<18}")

    for company in companies:
        company_id= company[0]
        company_name, eligible_students= get_company_eligible_students(company_id)

        eligible_count= len(eligible_students)

        if eligible_count >0:
            eligible_percentage=(eligible_count / total_students)*100
        else:
            eligible_percentage= 0

        if eligible_percentage > highest_percentage:
            highest_company= company_name
            highest_percentage= eligible_percentage

        print(f"{company_name:<24}"
              f"{total_students:<21}"
              f"{eligible_count:<19}"
              f"{eligible_percentage:.2f}")
    print()
    print(f"Company with Highest Eligibility: {highest_company}")
    print(f"Eligibility rate: {highest_percentage}")

