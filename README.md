# Placement Analytics Platform

A Python-based placement management system that helps manage student and company information, check student eligibility, and view basic placement analytics.

## About the Project

I developed this project to build a practical understanding of Python, Object-Oriented Programming, SQL, and database management.

The current version is a command-line application using Python and SQLite. It provides separate modules for student management, company management, eligibility checking, and analytics.

## Features

### Student Management
- Add student records
- View student records
- Update student information
- Delete student records
- Validate student details such as roll number, email, branch, CGPA, percentages, and graduation year

### Company Management
- Add company records
- View company details
- Update company information
- Delete company records
- Store company eligibility requirements
- Manage eligible branches for each company

### Eligibility Checker
The system checks whether students meet a company's requirements based on:

- CGPA
- Active backlogs
- Graduation year
- 10th percentage
- 12th percentage
- Branch

### Analytics
The analytics module provides basic information such as:

- Total students
- Total companies
- Average CGPA
- Students without active backlogs
- Company and eligibility-related information

## Technologies Used

- Python
- SQLite
- SQL
- Object-Oriented Programming
- Git
- GitHub

## Project Structure

```text
Placement_Analytics_Platform/
│
├── charts/
├── database/
├── reports/
│
├── analytics.py
├── analytics_menu.py
├── applications.py
├── company.py
├── company_menu.py
├── database.py
├── eligibility.py
├── eligibility_menu.py
├── main.py
├── student.py
├── student_menu.py
├── util.py
│
├── .gitignore
└── README.md
```
## How to use

### 1. Clone the repository
```bash
git clone <https://github.com/adarshkatgale/Placement-Analytics-Platform.git>
```
### 2. Open the project directory
```bash
cd Placement_Analytics_Platform
```
### 3. Run the application
```bash
python main.py
```
The application uses SQLite for data storage. The database is created locally when the application is initialized.

## Database

SQLite is used in the current version because it is lightweight and does not require a separate database server.

The local database file is excluded from the GitHub repository using .gitignore.

## Future Improvements

Some features planned for future versions include:
- Student data import and export
- Web-based interface
- Advanced analytics and visualizations
- FastAPI backend
- Authentication and role-based access
- Support for multiple users

## What I Learned

While developing this project, I worked with:
- Python classes and objects
- CRUD operations
- SQLite and SQL queries
- Database relationships
- Input validation
- Modular Python programming
- Eligibility and business logic
- Basic data analysis
- Git and GitHub

## Author
**Adarsh Sunil Katgale**
B.Tech – Electronics & Telecommunication Engineering