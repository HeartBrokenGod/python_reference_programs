
#  you cant add or substract strings

x = "Taj"
y = " Mahal"

print(x+y)

z = "Neel"*3

print(z)


#   use of slicing operator [:]
str1 = "niket"

print( str1[0:4] )

print(str1)

str2 = str1[2:]

print(str2)



#  strings are immutable
str3 = "aman"

str3 = "prajakta"

print(str3)

# normal ascii strings
ch = r"क"
print(ch)

# unicode string
chUnicode = u"क"
print(chUnicode)

# captalise function
str4 = "aman"

print( str4.capitalize() )
print( str4.upper() )

# isDigit function
str5 = "146.9"

if(str5.isdigit()):
    print("str5 contains all digits")
else:
    print("str5 donot contains all digits")

#len function
str6 = "Niket "

print("str6 lenth is ",len(str6))


# join function
maskingString = "****"

tup1 = ("9","49","93")

print(maskingString.join(tup1))


# replace function
str7 = "beautifooloo"

print(str7.replace("oo","u"))

print(str7)

str8 = "149.6"

numStr = str8.replace(".","",1)

if(numStr.isdigit()):
    num = float(str8)
    num = num + 30
    print("str8 is number and its modified value is ",num)

else:
    print("str8 is not number")

# aplha numeric checking function
str9 = "amanisC$$l"
if(str9.isalnum()):
    print("str9 is alpha numeric")

else:
    print("str9 is not alpha numeric")