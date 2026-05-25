# grading the students marks
student_name = input("Enter Your Name :")
print("welcome here")
marks = int(input("enter your marks:"))

if marks >= 70 and marks <= 100:
    print("A")
elif marks >= 60 and marks <= 70:
    print("B")
elif marks >= 50 and marks <= 60:
    print("C")
elif marks >= 40 and marks <= 50:
    print("D")
elif marks <= 39 and marks <= 40:
    print("fail")
else:
    print("invalid answer") 



