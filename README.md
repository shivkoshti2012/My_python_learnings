# 1. Student Data (Variables and Datatypes)
student_name = "Alex Mercer"  # str
roll_number = 101             # int
math_score = 92.5             # float
science_score = 88.0          # float
english_score = 79.5          # float

# 2. Checking Datatypes using type() and isinstance()
print("--- Type Verification Check ---")
print("Is student_name a string?", isinstance(student_name, str))
print("Is roll_number an integer?", isinstance(roll_number, int))
print("Type of math_score is:", type(math_score))
print("-------------------------------\n")

# 3. Calculations
total_marks = math_score + science_score + english_score
average_percentage = total_marks / 3

# 4. Printing the Report Card using print()
print("====================================")
print("         STUDENT REPORT CARD        ")
print("====================================")
print("Student Name:", student_name)
print("Roll Number: ", roll_number)
print("------------------------------------")
print("SUBJECTS       | MARKS OBTAINED")
print("------------------------------------")
print("Mathematics:   ", math_score)
print("Science:       ", science_score)
print("English:       ", english_score)
print("------------------------------------")
print("Total Marks:   ", total_marks)
print("Percentage:    ", average_percentage, "%")
print("====================================")
