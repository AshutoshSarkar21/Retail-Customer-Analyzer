Retail Customer Analyzer

Python Programming Project – PS No. 86

Institution: Rungta International Skills University
School: School of Information Technology
Course: Bachelor of Computer Application (BCA)
Developed by: Ashutosh Sarkar

---

1. Project Overview

Retail Customer Analyzer is a menu-driven Python application that analyzes customer spending data stored in a CSV file. It uses the Pandas library to calculate spending statistics, identify high-value customers, and generate city-wise spending summaries.

2. Project Objectives

- Analyze customer spending data.
- Calculate mean and median spending.
- Identify the highest and lowest spenders.
- Filter customers based on a user-entered spending limit.
- Generate city-wise total and average spending.
- Handle invalid user inputs and missing data files.

3. Features

1. Spending Statistics: Displays total customers, total spending, mean, median, highest spender, and lowest spender.
2. High-Value Customer Filtering: Lists customers whose total spending is at least the entered limit.
3. City-Wise Summary: Displays customer count, total spending, and average spending for each city.
4. Input Validation: Handles invalid text and negative spending limits.
5. CSV File Handling: Reads customer data and handles a missing CSV file.

4. Technologies Used

- Python 3
- Pandas
- CSV file handling
- Visual Studio Code

5. Project Files

File| Description
"one.py"| Complete Python source code
"customers.csv"| Customer spending dataset
"README.md"| Project documentation
"Retail_Customer_Analyzer_Test_Case_Screenshots.pdf"| Test execution screenshots

6. Requirements

- Python 3 installed.
- Pandas library installed.
- "one.py" and "customers.csv" must be in the same project folder.

Install Pandas using:

pip install pandas

7. How to Run the Project

1. Download or clone this repository.
2. Open the project folder in Visual Studio Code.
3. Ensure "one.py" and "customers.csv" are in the same folder.
4. Open the VS Code terminal.
5. Run the following command:

python one.py

6. Select an option from the displayed menu.
7. Enter the requested input.

8. Sample Dataset

The "customers.csv" file contains the following columns:

- CustomerID
- Name
- City
- Purchases
- TotalSpent

The dataset contains 8 sample customer records from Raipur, Bhilai, and Durg.

9. Test Cases and Results

The project was tested using all four prescribed test cases.

Test Case 1: Normal Input – Spending Statistics

Expected results:

- Total customers: 8
- Total spending: Rs. 73,000.00
- Mean spending: Rs. 9,125.00
- Median spending: Rs. 7,500.00
- Highest spender: Chitra (Rs. 25,000)
- Lowest spender: Deepak (Rs. 800)

Test Case 2: High-Value Customers

Input: Rs. 25,000

Expected result:

- Number of matching customers: 1
- C03 | Chitra | Raipur | Rs. 25,000.00

Test Case 3: Invalid Input

- Input "abc": Displays an invalid amount message.
- Input "-500": Displays a message that the limit cannot be negative.

Test Case 4: City-Wise Summary

Expected results:

- Raipur: Total Rs. 43,000 | Average Rs. 14,333.33
- Bhilai: Total Rs. 15,800 | Average Rs. 7,900.00
- Durg: Total Rs. 14,200 | Average Rs. 4,733.33

The corresponding execution screenshots are provided in the test case PDF.

10. Conclusion

The Retail Customer Analyzer demonstrates the use of Python, Pandas, filtering, grouping, and statistical calculations to analyze retail customer spending data. It provides useful spending insights through a simple menu-driven interface.

---

Developed by: Ashutosh Sarkar
Python Programming Project – PS No. 86
Rungta International Skills University
