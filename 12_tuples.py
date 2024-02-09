# A tuple is a built in data-type which is used to create immutable lists.
# A tuple is a collection of elements separated by commas and enclosed in parenthesis.
# A tuple is immutable, which means that once created, its elements cannot be changed.
# A tuple can be created without parenthesis as well.
# A tuple can contain different data-types.
# A tuple can be created using the tuple() constructor as well.
# A tuple can be accessed using indexing.
# A tuple can be sliced.
# A tuple can be concatenated.

age=(15,56,85,45,12,15)
print(age[0])

# empty tuple
emptyTuple=()
print(emptyTuple)
print(type(emptyTuple))

# tuple with one element
singleElementTuple=(1,)
print(singleElementTuple)

# slicing

print(age[1:4])

# methods in tuple

# index(element); returns the index of first occurence of value in tuple
print(age.index(85)) #2

# count(element); returns the number of occurences of value in tuple
print(age.count(15)) # 2