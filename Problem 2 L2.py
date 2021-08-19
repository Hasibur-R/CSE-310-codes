# 1. Create a list of 10 elements using list constructor
list=list((1,2,3,4,5,6,7,8,9,10))

# 2. Replace the element in index 1 with a new value
list[1]="0"
print(list)

# 3. Replace first 3 elements with 3 new values [Hints: use slicing]
list[:3]=[10,20,30]
print(list)

# 4. Replace first 3 elements with 2 new values
list[:3]=[11,22]
print(list)

# 5. Replace first 3 elements with 4 new values
list[:3]=[33,44,55,66]
print(list)

# 6. Insert a new element in index 3 using insert function 
list.insert(3,101)
print(list)

# 7. Remove an element from the list using remove function
list.remove(101)
print(list)

# 8. Remove the last element from the list
list.pop()
print(list)

# 9. Remove the second last element from the list
list.pop(-2)
print(list)

# 10.Remove the element at index 5 using del 
del list[5]
print(list)

# 11.Clear the list
list.clear()
print(list)

# 12.Delete the list permanently from the program A
del list