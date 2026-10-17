PASS_MARK=35
MIN_ATTENDANCE=75
def calculate_total(english_marks, maths_marks, dbms_marks):
    return english_marks + maths_marks + dbms_marks
def calculate_average(total_marks, number_of_subjects):
    return total_marks / number_of_subjects
def calculate_grade(average):
    if average >= 90:
        return "S"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= PASS_MARK:
        return "E"
    else:
        return "F"
def check_result(marks):
    if marks >= PASS_MARK:
        return "PASS"
    else:
        return "FAIL"
def get_performance_level(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Very Good"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Average"
    elif average >= PASS_MARK:
        return "Needs Improvement"
    else:
        return "Poor"