# sort of equivalent of arrays in other languages
# list is a collection of elements
# list is mutable whreas tuple and strings are immutable
# list is ordered
# list is heterogeneous
# list is dynamic
# list is indexed
# list is iterable
# list is subscriptable
# list is slicable
# list is concatenable
# list is reassignable


marks=[23,69,56,12,85]
print(type(marks))
print(marks)
print(marks[3])
newMarks=[1.3,65,85,45,"hello"] # we can store different types of data in a list
print(newMarks)
marks[4]=12000  # lists are mutable
print(marks);


# slicing 
print(marks[0:3])
print(marks[1:3])  
print(len(marks))

#  List methods
# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()


# append()
studentsMark=[12,36,2,45,85,63]
studentsMark.append(0)
print(studentsMark)

# sort()
studentsMark.sort()
print(studentsMark)
studentsMark.sort(reverse=True)
print(studentsMark)


# reverse()
studentsMark.reverse()
print(studentsMark)

# insert()
studentsMark.insert(6,"inserted");
print(studentsMark)

# remove()
studentsMark.remove("inserted")
print(studentsMark)

# .pop()
studentsMark.pop(0)
print(studentsMark)

# copy()
studentsMark.remove(45)
newUserMarks=studentsMark.copy()
print(newUserMarks)