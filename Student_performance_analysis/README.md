# Student Performance Analytics System

A Python project that analyzes student marks, grades, pass/fail results, attendance, and department-wise performance using **Pandas** and **NumPy**. The project includes a console-based analysis in `main.py` and reusable calculation functions in `functions.py`. An optional Streamlit dashboard can be run through `app.py` if that file is included in the project folder.

**Student:** C. Thejaswini  
**AICTE Student ID:** STU69b52638032e21773479480  
**Course:** Python with AI, EWB Courses

## Objective

The Student Performance Analytics System automates the analysis of student records. It calculates totals, averages, grades, individual subject results, and overall results. It also summarizes class performance, identifies top and lowest-performing students, compares subjects, analyzes attendance, and groups results by department.

## Technologies Used

- **Python 3** — program logic, conditions, loops, and reusable functions
- **Pandas** — CSV loading, DataFrame processing, sorting, filtering, and grouping
- **NumPy** — numerical statistics and overall pass/fail logic
- **Streamlit (optional dashboard)** — web-based interface, if `app.py` is included
- **Git and GitHub** — version control and project hosting

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | Runs the console-based analysis and prints detailed reports |
| `functions.py` | Defines reusable functions and shared thresholds for marks and attendance |
| `students_data.csv` | Dataset containing 25 student records |
| `app.py` | Optional Streamlit dashboard; include this file if you want to run the dashboard version |
| `README.md` | Project overview and setup instructions |
| `Project_Documentation.docx` | Detailed project documentation |
| `screenshots/` | Place screenshots of the program output or dashboard here |

## Dataset Description

The dataset is named **`students_data.csv`** and contains 25 student records. Marks are out of 100, and attendance is recorded as a percentage.

Required columns:

- `Roll_No` — unique student/roll number
- `Name` — student name
- `Department` — student's department
- `English` — English marks
- `Maths` — Mathematics marks
- `DBMS` — Database Management Systems marks
- `Attendance` — attendance percentage

Keep `students_data.csv` in the same folder as `main.py`, `functions.py`, and (if used) `app.py`.

## Installation

1. Install Python 3.
2. Open a terminal or command prompt in the project folder.
3. Install the required packages:

   ```bash
   pip install pandas numpy
   ```

4. To use the optional Streamlit dashboard, also install Streamlit and Matplotlib:

   ```bash
   pip install streamlit matplotlib
   ```

## How to Run

### Console version

Run the following command from the folder containing `main.py`:

```bash
python main.py
```

The program prints the student records, individual performance, class statistics, subject-wise statistics, attendance analysis, top three students, department-wise reports, and a complete analysis table.

### Optional Streamlit dashboard

If `app.py` is present in the project folder, run:

```bash
streamlit run app.py
```

The dashboard provides summary metrics, student records, subject-wise average marks, performance distribution, department summaries, the top three students, attendance information, CSV upload, and a download option for the analyzed data. The dashboard checks for required columns and reports missing or invalid data.

## Rules Used

### Passing criteria

- `PASS_MARK = 35`
- A student passes an individual subject when the marks are **35 or higher**.
- A student passes overall only when they score at least 35 in **all three subjects**: English, Maths, and DBMS.
- `MIN_ATTENDANCE = 75`; students with attendance **below 75%** are counted as low-attendance students.

### Grade scale

Grades are assigned based on the student's average marks:

| Average marks | Grade |
|---|---|
| 90 and above | S |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| 35 to below 50 | E |
| Below 35 | F |

### Performance levels

| Average marks | Performance level |
|---|---|
| 90 and above | Excellent |
| 80 to below 90 | Very Good |
| 70 to below 80 | Good |
| 60 to below 70 | Average |
| 35 to below 60 | Needs Improvement |
| Below 35 | Poor |

## Key Features

- Loads student records from `students_data.csv`
- Calculates total and average marks using reusable functions
- Assigns grades and performance levels
- Calculates individual subject and overall pass/fail results
- Reports class average, highest average, and lowest average
- Calculates subject-wise averages and identifies the best-performing subject
- Lists the top three performing students
- Reports average attendance and counts students below 75% attendance
- Produces department-wise student strength, pass/fail counts, and average marks
- Provides a complete analysis table in the console version
- Optional dashboard supports charts, CSV uploads, tables, and downloading analyzed data when `app.py` is included

## Sample Output Summary

For the supplied dataset, the console program reports:

```text
Total Students       : 25
Class Average        : 67.76
Highest Average      : 91.33
Lowest Average       : 36.67
Passed Students      : 19
Failed Students      : 6
Passing Mark         : 35

English Average      : 74.80
Maths Average        : 61.28
DBMS Average         : 67.20
Best Performing Subject: English

TOP 3 PERFORMING STUDENTS
1. P Keerthi - Average: 91.33 - Grade: S - Result: PASS
2. Yashwanth MK - Average: 90.33 - Grade: S - Result: PASS
3. A Hanipriya - Average: 89.33 - Grade: A - Result: PASS
```

*Sample statistics are based on the dataset supplied with the project. They will change if the CSV data is modified.*

## Final Outcome

The system automates student performance calculations and produces class-level, subject-level, attendance, and department-level summaries for the 25 records in the supplied dataset. In the current sample, 19 students pass overall and 6 fail overall. English has the highest subject average (74.80), while Maths has the lowest subject average (61.28).

## Screenshots

Add screenshots of the actual program output to the `screenshots/` folder. To make them easy for reviewers to view on GitHub, reference them in this README using relative paths, for example:

```markdown
![Console output](screenshots/console_output.png)
![Dashboard](screenshots/dashboard.png)
```

Use the actual screenshot filenames that you upload. The dashboard screenshot is applicable only if `app.py` is included and the dashboard has been run.

## GitHub Repository

https://github.com/thejaswini1707/Python_with_ai
