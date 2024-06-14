Expense Tracker Web Application
Introduction
Managing personal finances can often be a daunting task. To address this issue, we built an expense tracker web application using Python, HTML, and CSS. The primary goal of this project is to help users easily track their expenses, manage their budgets, and gain insights into their spending habits.

Features
Expense Logging: Users can log their expenses by entering details such as amount, category, date, and a description.
Expense History: View your expense history daily, monthly, and yearly to understand your spending patterns.
Budget Management: Set monthly budgets for different categories and track expenses against these budgets.
Technologies Used
Frontend: HTML5, CSS3, JavaScript
Backend: Python with Flask framework
Database: MySQL
Setup Instructions
Prerequisites
Ensure you have the following installed on your system:

Python 3.x
MySQL
pip (Python package installer)
Installation
Clone the repository

bash
Copy code
git clone https://github.com/Buchiken11/alx-expense-tracker-project.git
cd alx-expense-tracker-project.git
Install dependencies

bash
Copy code
pip install -r requirements.txt
Configure the database

Set up your MySQL database with the following credentials:

python
Copy code
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'buchiken'
app.config['MYSQL_PASSWORD'] = 'bbken'
app.config['MYSQL_DB'] = 'bblexpense'
Run the application

bash
Copy code
python app.py
Access the application

Open your web browser and go to http://localhost:5000.

Usage Guidelines
Logging Expenses

Navigate to the "Add Expense" page.
Enter the required details: amount, category, date, and a brief description.
Submit the form to log the expense.
Viewing Expense History

Use the navigation menu to view your expense history by day, month, or year.
Analyze your spending patterns and adjust your budgets accordingly.
Managing Budgets

Navigate to the "Budget Management" page.
Set your monthly budgets for different categories.
Track your expenses against these budgets and receive alerts when you are close to exceeding your limits.
About the Developer
My name is Kenechukwu Onyebuchi, and I am a Software Developereloper with a passion for creating web applications that solve real-world problems. With a strong foundation in Python and web technologies, I enjoy taking on challenging projects that allow me to grow my skills and contribute to meaningful solutions.

Feel free to connect with me on LinkedIn. https://www.linkedin.com/in/buchiken?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

Thank you for taking the time to learn about our expense tracker application. We hope you find it useful and look forward to any feedback or suggestions you may have.

Source code: https://github.com/Buchiken11/alx-expense-tracker-project.git
