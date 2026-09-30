name = input("Enter your name: ")
age = int(input("Enter your age: "))  # 1. Converted to int here
citizen = input("Tell your citizenship: ")

if age >= 18 and citizen == "India":  # 2. Fixed logic here
    if citizen == "India":
        print("You are eligible to vote")
    else:
        print("Get the citizenship first")
elif age <= 17 and citizen == "India":
    print("Get 18+ first")  # 3. Fixed spelling typo here
else:
    print("Enter into eligible age and Get citizenship of India")
