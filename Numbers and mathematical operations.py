num1 = 54
num2 = 56
num3 = 54.2
num4 = 56.8
#This will display type of data stored in variable.
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
#This will show the data which has been stored in variable
print(num1)
print(num2)
print(num3)
print(num4)
#addition, substraction, division and multiplication of integer numbers
add = num1 + num2
sub = num2 - num1
mul = num1 * num2
div = num2 / num1
print ("Addition of ",num1,"and ",num2,"is:",add)
print ("subtraction of ",num2,"and ",num1,"is:",sub)
print ("Multiplication of ",num1,"and ",num2,"is:",mul)
print ("Division of ",num2,"and ",num1,"is:",div)
#addition, substraction, division and multiplication of float numbers
add1 = num3 + num4
sub1 = num4 - num3
mul1 = num3 * num4
div1 = num4 / num3
print ("Addition of ",num3,"and ",num4,"is:",add1)
print ("subtraction of ",num4,"and ",num3,"is:",sub1)
print ("Multiplication of ",num3,"and ",num4,"is:",mul1)
print ("Division of ",num4,"and ",num3,"is:",div1)
#addition, subtraction, division and multiplication of float numbers and integer numbers
add2 = num1 + num3
sub2 = num3 - num1
mul2 = num1 * num3
div2 = num3 / num1
print ("Addition of ",num1,"and ",num3,"is:",add2)
print ("subtraction of ",num3,"and ",num1,"is:",sub2)
print ("Multiplication of ",num1,"and ",num3,"is:",mul2)
print ("Division of ",num3,"and ",num1,"is:",div2)
# % means the remainder of two number after division
div3 = num3%num1
print ("Remainder of ",num3,"and ",num1,"is:",div3)
#Floor Division
fdiv = num3//num1
print ("Floor Division of ",num3,"and ",num1,"is:",fdiv)
#Exponential
e1 = num1**num2
e2 = num3**num4
e3 = num1**2
e4 = num3**2
print(e1)
print(e2)
print(e3)
print(e4)
#change of data type i.e. integer to float and float to integer
num2_float1 = float(num2)
num4_int1 = int(num4)
print(type(num2_float1))
print(type(num4_int1))
print(num2_float1)
print(num4_int1)
#round()
roundnum3 = round(num3)
print(roundnum3)
#abs
num5 = -5
abnum5 = abs(num5)
#power
result1 = pow(2,4)
result2 = pow(2,4,6)
print(result1)
print(result2)