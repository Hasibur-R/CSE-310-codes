#Create an emply list
list = []

#Append 10 Random positive and negative integer into the list by taking as user inputs
for i in range(10):
  list.append(int(input()))

#Sort the list
list.sort()

#Sort in reverse order
list.sort(reverse = True)

#Sort the list using the absolute value of each integer [Hints: Using custom function]
def func(num):
  return abs(num)
list.sort(key = func)