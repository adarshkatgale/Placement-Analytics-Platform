from database import connection
from util import valid_comp_id,valid_num_branches,valid_cgpa,valid_backlogs,valid_graduation_year,get_valid_branch,get_valid_name,get_valid_percentage,valid_choice

class Company:

    def __init__(self,company_name, minimum_cgpa, maximum_backlogs, 
                 graduation_year, tenth_percentage, twelfth_percentage):
        self.company_name= company_name
        self.minimum_cgpa= minimum_cgpa
        self.maximum_backlogs= maximum_backlogs
        self.graduation_year=graduation_year
        self.tenth_percentage= tenth_percentage
        self.twelfth_percentage= twelfth_percentage


class CompanyManagement:

    def __init__(self, connection):
        self.connection= connection
        self.cursor= connection.cursor()

        
    def add_company_branches(self,company_id):
        number_of_branches= valid_num_branches()
            
        for i in range(number_of_branches):
            branch= get_valid_branch()
            self.cursor.execute("""
            INSERT INTO Company_Branches
            (Company_id, Branch)
            VALUES(?,?)
            """, (company_id, branch))

    def delete_company_branches(self,company_id):
        self.cursor.execute("""
        DELETE FROM Company_Branches
        WHERE Company_id= ?
        """, (company_id,))

    def insert_company(self):
        company_name= get_valid_name("Company")
        minimum_cgpa= valid_cgpa()
        maximum_backlogs= valid_backlogs()
        graduation_year= valid_graduation_year()
        tenth_percentage= get_valid_percentage('Tenth')
        twelfth_percentage= get_valid_percentage('Twelfth')

        company= Company(company_name, minimum_cgpa, maximum_backlogs,
                         graduation_year, tenth_percentage, twelfth_percentage)

        self.cursor.execute("""
        INSERT INTO Companies
        (Company_name, Minimum_cgpa, Maximum_backlogs_allowed, Graduation_year,
        Minimum_tenth_percentage, Minimum_twelfth_percentage)
        VALUES(?,?,?,?,?,?)
        """, (company.company_name, company.minimum_cgpa, company.maximum_backlogs, 
              company.graduation_year, company.tenth_percentage, company.twelfth_percentage))
        self.connection.commit()
        company_id= self.cursor.lastrowid

        self.add_company_branches(company_id)
        self.connection.commit()

        print("Company Added successfully")

    def view_companies(self):

        self.cursor.execute(" SELECT * FROM Companies")
        companies= self.cursor.fetchall()
        if not companies:
            print("No company found.")

        for company in companies:

            print("="*20)
            print(f"Company Name : {company[1]}")
            print(f"Minimum CGPA : {company[2]}")
            print(f"Maximum Backlogs Allowed : {company[3]}")
            print(f"Graduation Year : {company[4]}")
            print(f"Tenth Percentage: {company[5]}")
            print(f"Twelfth Percentage: {company[6]}")
            print("\nEligible Branches")
            self.cursor.execute("""
            SELECT Branch
            FROM Company_Branches
            WHERE Company_id= ?
            """, (company[0],))

            branches= self.cursor.fetchall()

            for branch in branches:
                print(f"• {branch[0]}")

            print("="*20)

    def show_companies(self):

        self.cursor.execute("SELECT Company_id, Company_name FROM Companies")
        companies= self.cursor.fetchall()
        if not companies:
            print("No company found")
            return    
        print("ALL COMPANIES")    
        print("="*20)
        for company in companies:
            print(f"ID:{company[0]} | {company[1]}")
        print("="*20)

    def update_company_field(self,new_value,company_id,column):
        self.cursor.execute(f"""
        UPDATE Companies
        SET {column}= ?
        WHERE Company_id=?
        """, (new_value,company_id))
        self.connection.commit()

    def update_company(self):
        self.show_companies()
        company_id= valid_comp_id()

        self.cursor.execute("""
        SELECT Company_id
        FROM Companies
        WHERE Company_id= ?
        """, (company_id,))
        company= self.cursor.fetchone()

        if company is None:
            print("Company not found!")
            return

        print("\nWhat do you want to update?")
        print("="*30)
        print("1. Company Name")
        print("2. Minimum CGPA")
        print("3. Maximum Backlogs Allowed")
        print("4. Graduation Year")
        print("5. Eligible Branches")
        print("6. Tenth percentage")
        print("7. Twelfth percentage")

        choice= valid_choice(7)

        if choice == 1:
            new_value= get_valid_name("New Company")
            column= "Company_name"
            self.update_company_field(new_value, company_id, column)

        elif choice == 2:
            new_value= valid_cgpa()
            column= "Minimum_cgpa"
            self.update_company_field(new_value, company_id, column)

        elif choice == 3:
            new_value = valid_backlogs()
            column= "Maximum_backlogs_allowed"
            self.update_company_field(new_value, company_id, column)

        elif choice == 4:
            new_value = valid_graduation_year()
            column= "Graduation_year"
            self.update_company_field(new_value, company_id, column)

        elif choice ==5 :
            self.delete_company_branches(company_id)
            self.add_company_branches(company_id)
            self.connection.commit()

        elif choice == 6:
                new_value = get_valid_percentage("Tenth")
                column= "Minimum_tenth_percentage"
                self.update_company_field(new_value, company_id, column)

        elif choice == 7:
                new_value = get_valid_percentage("TWelfth")
                column= "Minimum_twelfth_percentage"
                self.update_company_field(new_value, company_id, column)

        else:
            print("Please try again")
        print("Company updated Successfully")

    def delete_company(self):
        self.show_companies()
        company_id= valid_comp_id()
        self.delete_company_branches(company_id)

        self.cursor.execute("""
        DELETE FROM Companies
        WHERE Company_id= ?
        """, (company_id,))
        self.connection.commit()

        if self.cursor.rowcount== 0:
            print("Company not fount!")
        else:
            print("Company deleted successfully.")

