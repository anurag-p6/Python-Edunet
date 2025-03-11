import math

maths_marks = int(input("Enter the marks in Maths:"))
os_marks = int(input("Enter the marks in OS:"))
mechanical_marks = int(input("Enter the makrs in Mechanical"))
python_marks = int(input("Enter the marks in python:"))
java_marks = int(input("Enter the marks in java:"))

#marks is out of 20

if(maths_marks >= 8 and os_marks >=8 and mechanical_marks >=8 and python_marks >=8 and java_marks>=8):
  print("Congo you passed all subject")
else:
  print("Unfortunately you are fail")