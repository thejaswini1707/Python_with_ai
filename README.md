# Student Performance Analytics System
A Python data-analysis project that reads student records from a CSV file, processes them with **NumPy** and **Pandas**, and prints a clear report: totals, averages, grades, pass/fail results, subject-wise performance and top performers.

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

