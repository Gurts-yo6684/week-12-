# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#Lists are part of the collection family in Python
# Creating a list
mylist = [1,2, 3, 4, 5]
print(mylist) #[1, 2, 3, 4, 5,]
print(len(mylist)) #5
print(type(mylist))  # <class 'list>
print(mylist[0])#1
print(mylist[1:4])  #[2, 3, 4]
print(mylist[1:]) #[2, 3, 4, 5]
print(mylist[:-1]) # [1, 2, 3, 4]
#reverse a list
print(mylist[::-1]) #[5, 4, 3, 2, 1]
#Modifying a list 
mylist.append(6) # adds 6 to the end of the list
print(mylist)# [1, 2, 3, 4, 5, 6]
#add 7 and 8 to the end of the list
mylist.extend([7, 8])
print(mylist)#[1, 2, 3, 4, 5, 6, 7, 8]
#remove the last item
mylist.pop()
print(mylist) #[1, 2, 3, 4, 5, 6, 7]
#remove last 2 in index
mylist.pop(2)
print(mylist) #[1, 2, 4, 5, 6, 7]
#reverse the list
mylist.reverse()
print(mylist)#[7, 6, 5, 4, 2, 1]
#remove a speficic value
mylist.remove(4)
print(mylist) #[7, 6, 5, 2, 1]
#remove the last item using negative index
# add 50 more to the end of the list
new_list = list(range(12,120))
print(new_list)
mylist.append(new_list)
print(mylist)
# my list.extend
new_list = list(range(12,200))
print(new_list)
mylist.append(new_list)
print(mylist)
#print evrry 3 rd number
print(mylist[ : : 3])
# remove every 3rd item
del mylist[: : 3]
print(len(mylist))
print(mylist)


#list functions
# .append() - adds item to the end of the list
# .extend() - adds multiple items to the end of the list
# .pop() - removes and returns and item at a given index
#  (default id the last item)
# .remove() - removes the first occurrence of a specific value
#  .sort() - sorts the list in ascending order
# .reverse() - reverses the odrder of the list
# Why is a list more important than a variable?
###########################################################
# A list can hold multiple variables ,
# while a variable can only hold one value at a time
cakes = ['choclate', 'vanillia', 'red velvet', 'carrot']
print(cakes)
# access the first item
print(cakes[0]) #choclate
# access the last item
print(cakes[-1]) #carrot
#want to choclate instead of vanillia
cakes[0]= 'strabbery'
print(cakes) # straberry, vanillia, red velvet, carrot, lemon
#remove the last cake
cakes.pop()
print(cakes) #['strabery', 'choclate', 'red velvet']
# insert a new cake at index 2
cakes.insert(2, 'funfetti')
print(cakes)


#Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
foodslist = ['Quesabirrias', 'Chicken Alfredo', 'Vanillia Ice-Cream', 'Pizza', 'Chipotle']
print(foodslist)
# Print the second and last item.
print(foodslist())
# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.


#sets = {1, 2, 3}
# sets are unorders collections of unique items
# sets do not support indexing or slicing
# sets are mutable, meaning you can asdd or remove items
# sets are created using curely brakes{}
# Do sets not allow duplicates items? No, sets do not allow duplicates items
my_set = {1, 2, 3, 4, 5}
print(my_set) #{1, 2, 3, 4, 5}
print(type(my_set)) # <class 'set'>
# add an item to the set 












# tuples are ordered collections of tiems
# tuples are inmutable, meaning you cannot modify them after creation
# tuples are created using parethesis()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) #(1, 2, 3, 4, 5)
print(type(my_tuple)) # <class 'tuple'>
print(my_tuple[0]) # 1
print(my_tuple[1:4]) # ()
#try to modify the tuple (will raise an error)