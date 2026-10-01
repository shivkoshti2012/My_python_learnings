discount = 50  # Global variable

def sale(price):  # Accept price as an argument
    MRP = price - discount  # Local variable
    print(MRP)
    return MRP

# Pass a number (like 200) into the function when calling it
sale(200) 
