from company import CompanyManagement
from util import pause, print_headline, clear_screen, valid_roll_no,valid_comp_id
from database import connection, cursor

def get_company_eligible_students(company_id):
    cursor.execute("""
    SELECT * FROM Companies
    WHERE Company_id= ?
    """,(company_id,))

    company= cursor.fetchone()

    if company is None:
        return None,[]

    company_name= company[1]
    minimum_cgpa= company[2]
    maximum_backlogs= company[3]
    graduation_year= company[4]
    tenth_percentage= company[5]
    twelfth_percentage= company[6]

    cursor.execute("""
    SELECT Branch FROM
    Company_Branches
    WHERE Company_id=?
    """,(company_id,))

    branches= cursor.fetchall()
    eligible_branches= [branch[0] for branch in branches]

    cursor.execute("""
    SELECT * FROM Students
    """)
    students= cursor.fetchall()
    eligible_students=[]

    for student in students:
        if (student[5]>= tenth_percentage and
            student[6]>= twelfth_percentage and
            student[7]>= minimum_cgpa and
            student[9]== graduation_year and
            student[8]<= maximum_backlogs and
            student[4] in eligible_branches):
            eligible_students.append(student)

    return company_name, eligible_students


def company_eligibility_checker():
    print_headline("Company Wise Eligibility")
    company_management= CompanyManagement(connection)
    company_management.show_companies()

    company_id= valid_comp_id()

    company_name, eligible_students= get_company_eligible_students(company_id)

    if company_name is None:
        print("Company not found!")
        return

    print_headline(f"Eligible students for {company_name}")
    print(f"{'Roll no':<15}{'Name':<20}{'Branch':<12}{'CGPA':<8}")
    print("-"*70)

    for student in eligible_students:
        roll_no = student[1]
        name= student[2]
        branch= student[4]
        cgpa= student[7]
        print(f"{roll_no:<15}{name:<20}{branch:<12}{cgpa:<8}")

    if not eligible_students:
        print("No Eligible students found.")


def student_eligibility_checker():

    print_headline("Student wise Eligibility")

    roll_no= valid_roll_no()
    if roll_no is None:
        return 

    cursor.execute("""
    SELECT * FROM   Students
    WHERE Roll_no= ? 
    """,(roll_no,))

    student= cursor.fetchone()

    if student is None:
        print("student not found.")
        return

    student_name= student[2]
    student_branch= student[4]
    student_tenth_percentage= student[5]
    student_twelfth_percentage= student[6]
    student_cgpa= student[7]
    student_backlogs= student[8]
    student_graduation= student[9]

    cursor.execute("""
    SELECT * FROM Companies""")

    companies= cursor.fetchall()

    eligible_companies= []

    for company in companies:

        company_id= company[0]
        company_name= company[1]
        minimum_cgpa= company[2]
        maximum_backlogs= company[3]
        company_graduation_year= company[4]
        minimum_tenth_percentage= company[5]
        minimum_twelfth_percentage= company[6]

        cursor.execute("""
        SELECT Branch FROM Company_Branches
        WHERE Company_id=?
        """,(company_id,))
    
        branches= cursor.fetchall()
        eligible_branches= []
        for branch in branches:
            eligible_branches.append(branch[0])


        if (
            student_cgpa >= minimum_cgpa and
            student_backlogs <= maximum_backlogs and
            student_tenth_percentage >= minimum_tenth_percentage and
            student_twelfth_percentage >= minimum_twelfth_percentage and
            student_branch in eligible_branches and
            student_graduation == company_graduation_year
        ):
            eligible_companies.append(company_name)

    print_headline(f"Eligible companies for {student_name}")
    print(f"{'Roll No':<15}{'Name':<20}{'Branch':<12}{'CGPA':<8}")
    print("-"*70)
    print(f"{roll_no:<15}{student_name:<20}{student_branch:<12}{student_cgpa:<8}")
    if eligible_companies:
        print(f"Eligible Companies: {','.join(eligible_companies)}")
    else:
        print("No eligible company found.")

