# Define an empty list
list=[]


# Append 10 element into the list by taking as user inputs [ Hints: use a for loop]
for i in range(10):
    list.append(input())
print("\n")    
print("b.",list)


# Find out the datatype and length of the list
print("c.",type(list))
print(len(list))

# Show that the list is changable by writing update, add, remove operation on the list
list[1]="25"
print("d.",list)

list.append("11")
print(list)

list.pop(1)
print(list)

# Access the 2nd last element using the negative index
print("e.",list[-2])

# Create a new list by slicing the existing list from index 2 to 5(including)
print("f.",list[2:6])

# Create a new list by slicing the existing list from index 0 to 5(including)
print("g.",list[:6])

# Create a new list by slicing the existing list from index 5 to end of the list
print("h.",list[5:])

# Do the same task in 6 no question using negative index
print("i.", list[-8:-4])

# Do the same task in 6 no question using both positive and negative index
print("j.",list[-8:6])
print(list[2:-4])