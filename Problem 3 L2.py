# 1. Create a list of 10 elements using list constructor
list=list((1,2,3,4,5,6,7,8,9,10))

# 2. Print all items by referring to their index number [Hints use a for loop]
for i in range(len(list)):
    print(list[i])

# 3. Define an empty list
list1=[]

# 4. Append 10 Random Values (Integer Type) into the list by taking as user inputs [ Hints: use a for loop]
for i in range(10):
    list.append(int(input()))

# 5. Create a new list from the existing list by taking only the even number
list3=[]
for i in range(10):
    if i%2==0:
        list3.append(i)
print(list3)

# 6. Do the same task in question 5 using List comprehension 
new_list = [num for num in list1 if num%2 == 0]

# 7. Create a new list from the existing list by taking even number directly and replacing odd number as 0
new_list =[]
for num in list1:
  if num%2 == 0:
    new_list.append(num)
  else:
    new_list.append(0)

# 8. Do the same task in question 7 using List comprehension
new_list = [num if num%2 == 0 else 0 for num in list1 ]