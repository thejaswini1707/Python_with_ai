import pandas as pd
import numpy as np
import sys
from functions import (
    calculate_total, calculate_average, calculate_grade,
    check_result, get_performance_level, PASS_MARK, MIN_ATTENDANCE
)
print("=" * 60)
print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 60)
try:
    data = pd.read_csv("students_data.csv")
except FileNotFoundError:
    print("\nError: students.csv file was not found.")
    print("Make sure students.csv is in the same folder as main.py.")
    sys.exit()
print(data)
print("\n")
print("*" * 60)
print("DATASET INFORMATION")
print("*" * 60)
print("Total Students:", len(data))
print("Total Subjects:", 3)
print("\nAvailable Columns:")
print(list(data.columns))
# Total and average marks (using reusable functions from functions.py)
data["Total"] = data.apply(
    lambda row: calculate_total(row["English"], row["Maths"], row["DBMS"]), axis=1
)
data["Average"] = data["Total"].apply(lambda total: calculate_average(total, 3))
# Subject-wise pass/fail (pass mark is defined in functions.py)
data["English_Result"] = data["English"].apply(check_result)
data["Maths_Result"] = data["Maths"].apply(check_result)
data["DBMS_Result"] = data["DBMS"].apply(check_result)
# A student passes overall only if all three subjects are passed
data["Result"] = np.where(
    (data["English"] >= PASS_MARK) &
    (data["Maths"] >= PASS_MARK) &
    (data["DBMS"] >= PASS_MARK),
    "PASS",
    "FAIL"
)
data["Grade"] = data["Average"].apply(calculate_grade)
data["Performance"] = data["Average"].apply(get_performance_level)
print("\n")
print("*" * 60)
print("STUDENT PERFORMANCE")
print("*" * 60)
for index, student in data.iterrows():
    print(
        f"{student['Roll_No']} | "
        f"{student['Name']:<12} | "
        f"English: {student['English']:>3} ({student['English_Result']}) | "
        f"Maths: {student['Maths']:>3} ({student['Maths_Result']}) | "
        f"DBMS: {student['DBMS']:>3} ({student['DBMS_Result']}) | "
        f"Total: {student['Total']:>3} | "
        f"Average: {student['Average']:>6.2f} | "
        f"Grade: {student['Grade']:<2} | "
        f"Overall: {student['Result']}"
    )
class_average = np.mean(data["Average"])
highest_average = np.max(data["Average"])
lowest_average = np.min(data["Average"])
highest_student = data.loc[data["Average"].idxmax()]
lowest_student = data.loc[data["Average"].idxmin()]
passed_students = (data["Result"] == "PASS").sum()
failed_students = (data["Result"] == "FAIL").sum()
English_average = np.mean(data["English"])
maths_average = np.mean(data["Maths"])
dbms_average = np.mean(data["DBMS"])
subject_averages = {
    "English": English_average,
    "Maths": maths_average,
    "DBMS": dbms_average
}
best_subject = max(subject_averages, key=subject_averages.get)
english_passed = (data["English_Result"] == "PASS").sum()
english_failed = (data["English_Result"] == "FAIL").sum()
maths_passed = (data["Maths_Result"] == "PASS").sum()
maths_failed = (data["Maths_Result"] == "FAIL").sum()
dbms_passed = (data["DBMS_Result"] == "PASS").sum()
dbms_failed = (data["DBMS_Result"] == "FAIL").sum()
# Attendance and department-wise analysis
average_attendance = np.mean(data["Attendance"])
low_attendance_count = (data["Attendance"] < MIN_ATTENDANCE).sum()
top_students = data.sort_values(by="Average", ascending=False).head(3)
print("\n\n" + "*" * 60)
print("                 FINAL ANALYSIS")
print("*" * 60)
print("\n")
print("CLASS STATISTICS")
print("-" * 60)
print(f"Total Students       : {len(data)}")
print(f"Class Average        : {class_average:.2f}")
print(f"Highest Average      : {highest_average:.2f}")
print(f"Lowest Average       : {lowest_average:.2f}")
print("\nPASS / FAIL STATISTICS")
print("-" * 60)
print(f"Passed Students      : {passed_students}")
print(f"Failed Students      : {failed_students}")
print(f"Passing Mark         : {PASS_MARK}")
print("\nSUBJECT-WISE PASS / FAIL")
print("-" * 60)
print(f"English - Passed     : {english_passed}")
print(f"English - Failed     : {english_failed}")
print(f"Maths - Passed       : {maths_passed}")
print(f"Maths - Failed       : {maths_failed}")
print(f"DBMS - Passed        : {dbms_passed}")
print(f"DBMS - Failed        : {dbms_failed}")
print("\nATTENDANCE STATISTICS")
print("-" * 60)
print(f"Average Attendance   : {average_attendance:.2f}%")
print(f"Below {MIN_ATTENDANCE}% Attendance  : {low_attendance_count}")
print("\nHIGHEST PERFORMING STUDENT")
print("-" * 60)
print(f"Name                 : {highest_student['Name']}")
print(f"Student ID           : {highest_student['Roll_No']}")
print(f"Average              : {highest_student['Average']:.2f}")
print(f"Grade                : {highest_student['Grade']}")
print(f"Overall Result       : {highest_student['Result']}")
print("\nLOWEST PERFORMING STUDENT")
print("-" * 60)
print(f"Name                 : {lowest_student['Name']}")
print(f"Student ID           : {lowest_student['Roll_No']}")
print(f"Average              : {lowest_student['Average']:.2f}")
print(f"Grade                : {lowest_student['Grade']}")
print(f"Overall Result       : {lowest_student['Result']}")
print("\nSUBJECT-WISE PERFORMANCE")
print("-" * 60)
print(f"English Average      : {English_average:.2f}")
print(f"Maths Average        : {maths_average:.2f}")
print(f"DBMS Average         : {dbms_average:.2f}")
print(f"\nBest Performing Subject: {best_subject}")
print("\nTOP 3 PERFORMING STUDENTS")
print("-" * 60)
for rank, (index, student) in enumerate(top_students.iterrows(), start=1):
    print(
        f"{rank}. {student['Name']} - "
        f"Average: {student['Average']:.2f} - "
        f"Grade: {student['Grade']} - "
        f"Result: {student['Result']}"
    )
print("\n\n" + "*" * 60)
print("                 BRANCH-WISE REPORT")
print("*" * 60)
branch_columns = ["Roll_No", "Name", "English", "Maths", "DBMS",
                  "Attendance", "Total", "Average", "Grade", "Result"]
branch_summary = []
# Loop through each branch and show its students, strength and pass/fail count
for branch, branch_data in data.groupby("Department"):
    branch_strength = len(branch_data)
    branch_passed = (branch_data["Result"] == "PASS").sum()
    branch_failed = (branch_data["Result"] == "FAIL").sum()
    branch_average = np.mean(branch_data["Average"])
    print("\n" + "-" * 60)
    print(f"BRANCH: {branch}")
    print(f"Strength: {branch_strength} | Passed: {branch_passed} | "
          f"Failed: {branch_failed} | Branch Average: {branch_average:.2f}")
    print("-" * 60)
    print(branch_data[branch_columns].round(2).to_string(index=False))
    branch_summary.append([branch, branch_strength, branch_passed,
                           branch_failed, round(branch_average, 2)])
print("\n\nBRANCH SUMMARY")
print("-" * 60)
summary_table = pd.DataFrame(
    branch_summary,
    columns=["Branch", "Strength", "Passed", "Failed", "Average"]
)
print(summary_table.to_string(index=False))
print("\n\nCOMPLETE ANALYSIS TABLE")
print("=" * 60)
display_columns = [
    "Roll_No", "Name", "Department", "English", "English_Result",
    "Maths", "Maths_Result", "DBMS", "DBMS_Result",
    "Attendance", "Total", "Average", "Grade", "Result"
]
print(data[display_columns].to_string(index=False))
print("\n" + "*" * 60)
print("       ANALYSIS COMPLETED SUCCESSFULLY")
print("*" * 60)