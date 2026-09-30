import os
import re

def clear_screen():
    os.system("cls")

def pause():
    input("\nPlease press Enter...")

def print_headline(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)

""" Common Validations """

def get_valid_name(n):
    while True:
        name= input(f"Enter {n} name:")
        if not name.replace(" ","").isalpha():
            print("Invalid Name.\nPlease type your name.")
            continue
        return name

def get_valid_email():
    while True:
        email= input("Enter your email:")
        if email.endswith("@gmail.com") and " " not in  email:
            return email
        print("Invalid Email.\nPlease enter valid email.")

def get_valid_branch():
    ValidBranch= ['CSE','IT','EXTC','MECH','CIVIL','AI']

    while True:
        branch= input("Enter your Branch(CSE|IT|EXTC|MECH|CIVIL|AI): ")
        branch= branch.upper()
        if branch in ValidBranch:
            return branch
        print("Invalid Branch.\nPlease enter the branch.")

def get_valid_percentage(label):
    while True:
        try:
            percenage= float((input(f"Enter the {label} percentage:")))
            if 0<= percenage <=100:
                return percenage
            print("Please enter valid percentage between 0 to 100.")

        except ValueError:
            print("Invalid Number.,\nPlease enter a number.")

def valid_cgpa():
    while True:
        try:
            cgpa= float(input("Enter the CGPA:"))
            if 0<= cgpa <=10:
                return cgpa
            print("Please enter valid number between 0 to 10.")

        except ValueError:
            print("Invalid Number.\nPlease enter the number.")

def valid_backlogs():
    while True:
        try:
            backlogs= int(input("Enter the Backlogs:"))
            if backlogs >=0:
                return backlogs
            print("Please enter the proper number. ")

        except ValueError:
            print("Please enter the number.")


def valid_graduation_year():
    while True:
        try:
            graduation= int(input("Enter the graduation year:"))
            if 2027<= graduation <= 2030:
                return graduation
            print("Invalid year.")
            print("Please enter valid graduation year.")

        except ValueError:
            print("Please enter a number.")

def valid_roll_no():
    pattern= r"^\d{2}BT(ET|CS|IT|AI|CE|ME)\d{4}$"
    while True:
    
        roll_no= input("Enter the Roll number(or B/b to go back):")
        if roll_no== 'b' or roll_no== 'B':
            return None
        roll_no= roll_no.upper()
        if not re.fullmatch(pattern, roll_no):
            print("Invalid Roll No format.")
            pause()
            continue
        break
    return roll_no

def valid_choice(num):
    while True:
        choice= input("Enter the choice num:")
        if num ==3:
            if choice in ['1','2','3']:
                return int(choice)
            else:
                print("Invalid choice, Please try again.")
        elif num== 5:
            if choice in ['1','2','3','4','5']:
                return int(choice)
            else:
                print("Invalid choice, Please try again.")
        elif num==7:
            if choice in ['1','2','3','4','5','6','7']:
                return int(choice)
            else:
                print("Invalid choice, Please try again.")

def valid_num_branches():
    while True:
        try:
            num= int(input(f"Enter the number of branches btn 1 to 6:"))
            if num >0 and num<=6:
                return num
            else:
                print("Please select branch between 1 to 6.")
        except ValueError:
            print("Invalid input.")

def valid_comp_id():
    while True:
        try:
            id= int(input("Enter the company ID:"))
            if id>0 :
                return id
            else:
                print("Invalid ID.")
        except ValueError:
            print("Invalid input.")
