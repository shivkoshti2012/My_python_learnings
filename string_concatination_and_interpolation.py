Product_ame = "Soap"
price = 28

# Fix 1: Convert number to string for concatenation or put text in quotes
print(Product_ame + " price is " + str(price))

# Fix 2: Wrap the f-string inside proper quotation marks
print(f"{Product_ame} price is {price}")
