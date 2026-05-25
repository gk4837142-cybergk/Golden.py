# Student Grading System with Multiple Subjects, Students, and Averages

def grade_student(marks):
    """Return grade and remarks based on marks."""
    if marks >= 80 and marks <= 100:
        return "A", "Excellent performance"
    elif marks >= 70 and marks <= 79:
        return "B", "Very good work"
    elif marks >= 60  and marks <= 69:
        return "C", "Good effort"
    elif marks >= 50 and marks <= 59:
        return "D", "Fair, needs improvement"
    elif marks > 100:
        return "Invalid", "Marks cannot exceed 100"
    else:
        return "E", "Poor, work harder"

def print_receipt(name, subjects, results, avg_marks, avg_grade, avg_remarks):
    """Prints a receipt-style output for the student."""
    print("\n========== STUDENT GRADE RECEIPT ==========")
    print(f"Student Name : {name}")
    print("-------------------------------------------")
    for subject, (marks, grade, remarks) in zip(subjects, results):
        print(f"{subject:<12} | Marks: {marks:<3} | Grade: {grade} | {remarks}")
    print("-------------------------------------------")
    print(f"Average Marks : {avg_marks:.2f}")
    print(f"Average Grade : {avg_grade}")
    print(f"Remarks       : {avg_remarks}")
    print("===========================================\n")

# Main Program
if __name__ == "__main__":
    subjects = [
        "Math", "English", "Kiswahili", "Biology", "Chemistry",
        "Physics", "History", "Geography", "Computer"
    ]

    while True:
        student_name = input("\nEnter student name (or type 'no' to stop): ")
        if student_name.lower() == "no":
            print("\nGrading finished. Goodbye!")
            break

        results = []
        total_marks = 0

        for subject in subjects:
            marks = int(input(f"Enter marks for {subject}: "))
            grade, remarks = grade_student(marks)
            results.append((marks, grade, remarks))
            total_marks += marks

        # Calculate average marks
        avg_marks = total_marks / len(subjects)
        avg_grade, avg_remarks = grade_student(avg_marks)

        print_receipt(student_name, subjects, results, avg_marks, avg_grade, avg_remarks)


