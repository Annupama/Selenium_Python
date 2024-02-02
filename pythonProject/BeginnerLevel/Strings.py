str = "AmazonOnline.com"
str1 = "OnlineShopping Site"
str3 = "AmazonOnline"
print(str[1])    # m
print(str[0:6])   # If we want substring in python
print(str+str1)  # Concatenation
print(str3 in str)   # Substring check

var = str.split(".")  # Split the string
print(var)
print(var[0])

str2 = " products "   # Strip or trim the string
print(str2.strip())
print(str2.lstrip())   # trim the string at left side
print(str2.rstrip())   # trim the string at right side