a=input("Enter first name: ")
b=input("Enter second name: ")

full=a+" "+b
print(full)


#a. Find the number of occurrence ‘a’ in the Full name
print("a.",full.count('a'))


#b. Replace all the occurrence of ‘a’ with ‘u’ in the Full name
print("b.",full.replace('a','u'))


#c. Find the index of first occurrence of ‘a’ in the Full name
print("c.",full.find('a'))


#d. Slice the first 3 char of the first name.
print("d.",a[:3])


#e. Print the 2 nd last char of the last name.
print("e.",b[-2])