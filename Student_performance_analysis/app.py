from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

from functions import (
    calculate_total,
    calculate_average,
    calculate_grade,
    check_result,
    get_performance_level,
    PASS_MARK,
    MIN_ATTENDANCE,
)

SUBJECTS = ["English", "Maths", "DBMS"]
PERFORMANCE_ORDER = [
    "Excellent", "Very Good", "Good",
    "Average", "Needs Improvement", "Poor",
]

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide",
)


def show_table(df):
    """Show a full-width dataframe on both old and new Streamlit versions."""
    try:
        st.dataframe(df, width="stretch")
    except Exception:
        st.dataframe(df, use_container_width=True)


st.title("📊 Student Performance Analytics System")
st.write(
    "Analyze student marks, grades, attendance, "
    "department performance, and pass/fail results."
)

# ---------------------------------------------------------------------------
# Load and validate data
# ---------------------------------------------------------------------------
dataset_path = Path(__file__).with_name("students_data.csv")

uploaded_file = st.file_uploader(
    "Upload another student dataset (CSV)",
    type=["csv"],
)

try:
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_csv(dataset_path)

    required_columns = [
        "Roll_No", "Name", "Department",
        "English", "Maths", "DBMS", "Attendance",
    ]

    missing = [c for c in required_columns if c not in data.columns]
    if missing:
        st.error(
            "The dataset is missing these columns: " + ", ".join(missing)
        )
        st.stop()

    # Remember the original columns before new ones are calculated.
    original_columns = list(data.columns)

    numeric_columns = SUBJECTS + ["Attendance"]
    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column], errors="raise")

except FileNotFoundError:
    st.error(
        "students_data.csv was not found. "
        "Upload a CSV dataset to continue."
    )
    st.stop()
except (ValueError, pd.errors.ParserError, pd.errors.EmptyDataError) as error:
    st.error(f"Could not read the dataset: {error}")
    st.stop()

if data.empty:
    st.warning("The dataset contains no student records.")
    st.stop()

if data[numeric_columns].isna().any().any():
    st.error(
        "The dataset has empty marks or attendance values. "
        "Please fix them and upload the file again."
    )
    st.stop()

if not data[numeric_columns].apply(lambda col: col.between(0, 100)).all().all():
    st.error(
        "Marks and attendance must all be between 0 and 100. "
        "Please fix the dataset and upload it again."
    )
    st.stop()

# ---------------------------------------------------------------------------
# Calculations (same logic as main.py, using functions.py)
# ---------------------------------------------------------------------------
data["Total"] = data.apply(
    lambda row: calculate_total(row["English"], row["Maths"], row["DBMS"]),
    axis=1,
)
data["Average"] = data["Total"].apply(
    lambda total: calculate_average(total, len(SUBJECTS))
)

for subject in SUBJECTS:
    data[f"{subject}_Result"] = data[subject].apply(check_result)

data["Result"] = np.where(
    (data["English"] >= PASS_MARK)
    & (data["Maths"] >= PASS_MARK)
    & (data["DBMS"] >= PASS_MARK),
    "PASS",
    "FAIL",
)

data["Grade"] = data["Average"].apply(calculate_grade)
data["Performance"] = data["Average"].apply(get_performance_level)

# ---------------------------------------------------------------------------
# Dataset information
# ---------------------------------------------------------------------------
st.subheader("Dataset Information")
st.write(f"**Total Students:** {len(data)} | **Total Subjects:** {len(SUBJECTS)}")
st.write("**Available Columns:**", ", ".join(original_columns))

# ---------------------------------------------------------------------------
# Class statistics
# ---------------------------------------------------------------------------
passed = int((data["Result"] == "PASS").sum())
failed = int((data["Result"] == "FAIL").sum())

st.subheader("Class Statistics")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Students", len(data))
c2.metric("Class Average", f"{data['Average'].mean():.2f}")
c3.metric("Highest Average", f"{data['Average'].max():.2f}")
c4.metric("Lowest Average", f"{data['Average'].min():.2f}")

c5, c6, c7 = st.columns(3)
c5.metric("Passed", passed)
c6.metric("Failed", failed)
c7.metric("Passing Mark", PASS_MARK)

# ---------------------------------------------------------------------------
# Student records
# ---------------------------------------------------------------------------
st.subheader("Student Records")
show_table(data)

# ---------------------------------------------------------------------------
# Highest / lowest performing student
# ---------------------------------------------------------------------------
highest_student = data.loc[data["Average"].idxmax()]
lowest_student = data.loc[data["Average"].idxmin()]

h_col, l_col = st.columns(2)
with h_col:
    st.subheader("Highest Performing Student")
    st.write(f"**{highest_student['Name']}** ({highest_student['Roll_No']})")
    st.write(
        f"Average: {highest_student['Average']:.2f} | "
        f"Grade: {highest_student['Grade']} | "
        f"Result: {highest_student['Result']}"
    )
with l_col:
    st.subheader("Lowest Performing Student")
    st.write(f"**{lowest_student['Name']}** ({lowest_student['Roll_No']})")
    st.write(
        f"Average: {lowest_student['Average']:.2f} | "
        f"Grade: {lowest_student['Grade']} | "
        f"Result: {lowest_student['Result']}"
    )

# ---------------------------------------------------------------------------
# Subject-wise analysis
# ---------------------------------------------------------------------------
st.subheader("Subject-wise Average Marks")
subject_averages = data[SUBJECTS].mean()
st.bar_chart(subject_averages)
st.write(f"**Best Performing Subject:** {subject_averages.idxmax()}")

st.subheader("Subject-wise Pass / Fail")
subject_pass_fail = pd.DataFrame(
    {
        subject: {
            "Passed": int((data[f"{subject}_Result"] == "PASS").sum()),
            "Failed": int((data[f"{subject}_Result"] == "FAIL").sum()),
        }
        for subject in SUBJECTS
    }
).T
show_table(subject_pass_fail)

# ---------------------------------------------------------------------------
# Performance distribution
# ---------------------------------------------------------------------------
st.subheader("Student Performance Distribution")
performance_counts = (
    data["Performance"]
    .value_counts()
    .reindex(PERFORMANCE_ORDER, fill_value=0)
)
st.bar_chart(performance_counts)

# ---------------------------------------------------------------------------
# Top 3 students
# ---------------------------------------------------------------------------
st.subheader("Top 3 Performing Students")
top_students = data.nlargest(3, "Average")[
    ["Roll_No", "Name", "Department", "Average", "Grade", "Result"]
].round(2)
show_table(top_students)

# ---------------------------------------------------------------------------
# Attendance
# ---------------------------------------------------------------------------
st.subheader("Attendance")
a1, a2 = st.columns(2)
a1.metric("Average Attendance", f"{data['Attendance'].mean():.2f}%")

low_attendance = data[data["Attendance"] < MIN_ATTENDANCE]
a2.metric(f"Below {MIN_ATTENDANCE}% Attendance", len(low_attendance))

if low_attendance.empty:
    st.success(f"No students are below {MIN_ATTENDANCE}% attendance. 🎉")
else:
    show_table(
        low_attendance[["Roll_No", "Name", "Department", "Attendance"]]
    )

# ---------------------------------------------------------------------------
# Department / branch-wise report
# ---------------------------------------------------------------------------
st.subheader("Department-wise Summary")
department_summary = (
    data.groupby("Department")
    .agg(
        Strength=("Roll_No", "count"),
        Passed=("Result", lambda x: (x == "PASS").sum()),
        Failed=("Result", lambda x: (x == "FAIL").sum()),
        Average=("Average", "mean"),
    )
    .round(2)
)
show_table(department_summary)

st.subheader("Branch-wise Report")
branch_columns = [
    "Roll_No", "Name", "English", "Maths", "DBMS",
    "Attendance", "Total", "Average", "Grade", "Result",
]
for branch, branch_data in data.groupby("Department"):
    branch_passed = int((branch_data["Result"] == "PASS").sum())
    branch_failed = int((branch_data["Result"] == "FAIL").sum())
    with st.expander(f"{branch} ({len(branch_data)} students)"):
        st.write(
            f"Strength: {len(branch_data)} | Passed: {branch_passed} | "
            f"Failed: {branch_failed} | "
            f"Branch Average: {branch_data['Average'].mean():.2f}"
        )
        show_table(branch_data[branch_columns].round(2))

# ---------------------------------------------------------------------------
# Complete analysis table
# ---------------------------------------------------------------------------
st.subheader("Complete Analysis Table")
display_columns = [
    "Roll_No", "Name", "Department",
    "English", "English_Result",
    "Maths", "Maths_Result",
    "DBMS", "DBMS_Result",
    "Attendance", "Total", "Average", "Grade", "Performance", "Result",
]
show_table(data[display_columns].round(2))

# ---------------------------------------------------------------------------
# Download
# ---------------------------------------------------------------------------
csv_data = data.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Analysis as CSV",
    data=csv_data,
    file_name="student_performance_analysis.csv",
    mime="text/csv",
)

st.caption(
    f"Pass mark: {PASS_MARK}/100 per subject. "
    f"Attendance threshold: {MIN_ATTENDANCE}%."
)