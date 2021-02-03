

#  empty list
list_1 = []

# integer list
list_2 = [1, 2, 3, 4]
print(type(list_2))

# float list
list_3 = [1.1, 2.2, 3.3, 4.4]
print(type(list_3))

#   string list
list_4 = ["Neel", "Aman", "juhi"]
print(type(list_4))

#   mixed list
list_5 = ["Niket", 361, 55.98]
print(list_5)

#   nested list
list_6 = [ list_2, [33, 65, 89], list_4 ]
print(list_6)

# length of list
print( len(list_4) )

#   concatenation
list_7 = list_2 + list_3
print( list_7)

#   repeation of element in list
list_8 = ["Juhi"] * 10
print(list_8)

# check if the element is present in the list
if 360 in list_5:
    print("yes, 360 exist in  the list_5")
else:
    print("no, 360 does not exist in  the list_5")

#   iteration
for x in list_5:
    print(x)

#   list index
list_9 = ["neel","niket","aman"]
print( list_9[1] )

# nested list index
list_10 = ["neel",list_9,"juhi"]
print(list_10[1][2])

# negative index
print(list_9[-3])

# list slicing
list_11 = [ 5, 9, 6, 4, 3, 7 ]
print( list_11[3:] )

# list function
list_12 = [ 5, 9, 6, 4, 3, 7 ]
print(list_12)

# append an element to list
list_12.append(333)
print(list_12)

# append another list to list
list_12.extend(list_11)
print(list_12)

# insert a new element to list at specific index
list_12.insert(8,888)
print(list_12)

# removes the value from the list
list_12.remove(333)
print(list_12)

deletedElement  =  list_12.pop(7)
print(list_12)
# print(deletedElement)


# clear the list
list_12.clear()
print(list_12)

list_12.extend(list_11)
print(list_12)

# index func searches in the list for the element and return the index of the element
# if not found it throws an error
print( list_12.index(3) )

# count how many times the element is repeated in the list
list_13 = [1, 2, 3, 9, 8, 6, 3]
print( list_13.count(3) )

# sort function sorts the list in ascending or descending
list_14 = [44, 65, 21, 11, 9, 4, 31]
print(list_14)
list_14.sort(reverse=True)
print(list_14)

# reverses the list
list_14.reverse()
print(list_14)

# copy
list_15 = [1, 2, 3]
# we are assigning the copy of list_15 to list_16
list_16 = list_15.copy()
print(list_16)

# changes made to list_15
list_15.append(55)
# changes not reflected in the list_16 because we made a copy of list_15 and then assigned that copy to list_16
print(list_16)

