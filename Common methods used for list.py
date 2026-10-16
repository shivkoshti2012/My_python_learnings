numbers = [1,2,3,4,5,6]

# 1. append method
numbers.append(6)
print("Append:", numbers)

# 2. extend method (FIXED: changed 'extent' to 'extend')
number = [7,8,9]
numbers.extend(number) 
print("Extend:", numbers)

# 3. insert method
numbers.insert(2,2.5)
print("Insert:", numbers)

# 4. remove method
numbers.remove(8)
print("Remove:", numbers)

# 5. pop method
numbers.pop(2)
print("Pop:", numbers)

# 6. clear list
numbers.clear()
print("Clear:", numbers)

# 7. sort method
number1 = [2,3,5,6,1,7]
number1.sort()
print("Sort method:", number1)

# 8. sorted method
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)
print("Original list after sorted():", numbers)
print("New sorted list:", sorted_numbers)

# 9. Reverse method
sorted_numbers.reverse()
print("Reverse:", sorted_numbers)

# 10. index method (FIXED: stored and printed the index)
programming_languages = ['Rust', 'Java', 'Python', 'C++']
java_idx = programming_languages.index('Java')
print("Index of Java:", java_idx)

# FIXED: Handled missing item using an 'if' check to prevent a ValueError crash
if 'JavaScript' in programming_languages:
    js_idx = programming_languages.index('JavaScript')
    print("Index of JavaScript:", js_idx)
else:
    print("JavaScript was not found in the list.")
