# Student Performance Analytics System

A Python data-analysis project that reads student records from a CSV file, processes them with **NumPy** and **Pandas**, and prints a clear report: totals, averages, grades, pass/fail results, subject-wise performance and top performers.

**Student:** [Your Name] | **Roll No:** [Your Roll No] | **Course:** Python with AI (EWB Courses)

## Objective
Teachers often need a quick summary of how a class performed. This project automates that: it calculates each student's total, average, grade and result, and answers questions such as *Who scored highest? Which subject is strongest? How many students passed?*

## Technologies Used
- Python 3
- NumPy (numerical calculations)
- Pandas (loading and analysing data with DataFrames)

## Project Structure
| File | Purpose |
|------|---------|
| `main.py` | Runs the project and prints the full analysis |
| `functions.py` | Reusable functions (total, average, grade, pass/fail, performance level) |
| `students.csv` | Dataset of 25 students |
| `README.md` | Project documentation |
| `Project_Documentation.docx` | Detailed project documentation |

## Dataset
`students.csv` has **25 records** with these columns:

`Roll_No`, `Name`, `Department`, `English`, `Maths`, `DBMS`, `Attendance`

Marks are out of 100 and attendance is a percentage.

## How to Run
1. Install Python 3 and the required libraries:
   ```bash
   pip install pandas numpy
   ```
2. Keep `main.py`, `functions.py` and `students.csv` in the same folder.
3. Run:
   ```bash
   python main.py
   ```

## Rules Used
**Pass condition:** a student passes only if they score **40 or more in every subject** (English, Maths and DBMS).

**Grading (based on average marks):**
| Average | Grade |
|---------|-------|
| 90 and above | A+ |
| 80 - 89.99 | A |
| 70 - 79.99 | B |
| 60 - 69.99 | C |
| 50 - 59.99 | D |
| 40 - 49.99 | E |
| Below 40 | F |

## Key Features
- Loads and displays the dataset with Pandas, with a check for a missing file
- Calculates total and average marks for every student
- Assigns grades and performance levels using reusable functions
- Subject-wise and overall pass/fail results
- Class average, highest and lowest average (NumPy `mean`, `max`, `min`)
- Subject-wise averages and best-performing subject
- Top 3 students
- Attendance summary (average attendance, students below 75%)
- Department-wise average using Pandas `groupby`

## Sample Output (summary)
```
Total Students       : 25
Class Average        : 67.76
Highest Average      : 91.33
Lowest Average       : 36.67
Passed Students      : 18
Failed Students      : 7

English Average      : 74.80
Maths Average        : 61.28
DBMS Average         : 67.20
Best Performing Subject: English

TOP 3 PERFORMING STUDENTS
1. P Keerthi - Average: 91.33 - Grade: A+ - Result: PASS
2. Yashwanth MK - Average: 90.33 - Grade: A+ - Result: PASS
3. A Hanipriya - Average: 89.33 - Grade: A - Result: PASS
```

## Final Outcome
The program runs without errors and produces a complete, readable analysis of the class. Of 25 students, 18 passed and 7 failed; English was the best-performing subject and Maths the weakest.

## GitHub Repository
[Add your repository link here]
