num1 = 28
num2 = 30
#comparative Operator
print(num1==num2)
print(num1!=num2)
print(num1>=num2)
print(num1<=num2)
print(num1>num2)
print(num1<num2)
#if
if num1>num2:
    print(num1,"is greater than ",num2)
print(num1,"is less than ",num2)
#if...else
if num1<num2:
    print(num1,"is less than ",num2)
else:
    print(num1,"is greater than ",num2)
#if..elif..else
if num1>num2:
    print(num1,"is greater than ",num2)
elif num1<num2:
    print(num1,"is less than ",num2)
else:
    print(num1,"is equal to ",num2)
#nested if...else
if num1>=num2:
    if num1>num2:
        print(num1,"is greater than ",num2)
    else:
        print(num1,"is equal to ",num2)
else:
    if num1<num2:
        print(num1,"is less than ",num2)
    else:
        print(num1,"is equal to ",num2)