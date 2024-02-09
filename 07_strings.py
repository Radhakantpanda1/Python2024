# sequence of characters
# string is a collection of characters
# string is immutable
str1="This is a string"
str2=' This is also a string'
str3='''This is a multiline string'''
str4="""This is also a multiline string"""


# escape sequence characters
# \n => new line
# \t => tab
# \b => backspace
# \r => carriage return
# \f => form feed
# \a => alert

# \v => vertical tab

# string concatenation
print(str1+str2)

# len-
print(len(str1))

# indexing- string in python has indexing
# indexing starts from 0
# indexing is like array
print(str1[3])

for i in str1:
  print(i)

# slicing -accessing part of string
print(str1[0:5])

print(str2[5:len(str2)])
