str1 = "Hello World!, fghf"
str2 = "15348"
str3 = "AbCdE"
str4 = "faf12"
str5 = "Hello\tworld"
str6 = "aaaaaHello World!"  
sep = '*'

# print(str1[:2])

print(str1.capitalize())

# print(str1.center(20, '.')) 
# print(str1.center(20)) # defalut space 

# print(str1.count("o"))
# print(str1.count("o", 5))
# print(str1.count("o", 5, 7))  #  , strating index , ending index

# print(str1.encode('utf_16','strict'))
# encode = str1.encode('utf_16','strict')
# print(str1.encode('ascii','strict'))  # base64, ascii, gbk, hz, iso2022_kr, utf_32

# print(encode.decode('utf_16','strict'))
# print(str1.encode('ascii','strict'))  # base64, ascii, gbk, hz, iso2022_kr, utf_32

# print(str1.endswith("d!"))  
# print(str1.endswith("l",5 ,10))  #  , strating index , ending index

# print(str1.startswith("He"))   
# print(str1.startswith("l",3 ,10))  #  , strating index , ending index

# print(str5.expandtabs(5))

# print(str1.find("o"))   #  , strating index , ending index

# print(str1.index("o"))   #  , strating index , ending index

# print(str4.isalnum())  # A-z 0-9

# print(str4.isalpha())  # A-z

# print(str2.isdigit())  # 0-9

# print(str1.islower())

# print(str1.isupper()) 

# print(str2.isnumeric())

# print(str2.isspace())  # \t, \n, \v is true

# print(str1.istitle()) # after space word upper case

# print(sep.join(str1))

# print(len(str1))

# print(str1.ljust(20, '_'))

# print(str1.upper())

# print(str1.lower())

print(str6.lstrip('a'))

# print(max(str1))

# print(min(str2))

# print(str1.replace('o','0',1))  # 1 is change time of o-0

# print(str1.split(',')[0][0:2])

# print(str3.swapcase())

# print(str1.title())

# print(str1.zfill(20))