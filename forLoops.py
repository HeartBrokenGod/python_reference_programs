#   simple for loops
for i in range(10):
    print("Hello "+str(i))

#   advance for loop to loop over a list
list1 = ["Neel", "Sherlock", "Shinchan"]
for elem in list1:
    print(elem)

#   break keyword can break the for loop
for i in range(0, 10):
    print(i)
    if i == 4:
        break

#   continue keyword can skip the code for the perticular iteration
for i in range(10):
    if i == 4:
        continue
    print(i)
