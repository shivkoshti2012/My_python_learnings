num = input("Enter a number")
num1 = input("Enter 2nd number")
add = int(num) + int(num1)
print(add)
print("This is done by input function\n")
def sum(a,b):
    sum1 = a + b
    print("This is done by function")
    return sum1
hello = sum(2,3)
print(hello)