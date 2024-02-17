# List methods in python.

list1 = [2, 3, 5, 7, 9, 4]
list2 = ['mango', 'orange', 'guava', 'grapes']

list1.extend(list2)
# The ".extend()" function add two lists together making the one.
print(list1)

# Adding a new value.
list2.append('apple')
print(list2)

# Getting the "length" of the list.
print(len(list1))
print(len(list2))

# inserting a value inbetween two other values in a list. We use the ".insert()" function to perform the task. eg:

schools = list(('Konigin', 'Boys Sec. Sch.', 'St rita', 'marin'))
schools.insert(2, 'Idaw river')
print(schools)
# The inserts accepts only two argument to be parsed.

#To remove a value from the list.
schools.remove('Boys Sec. Sch.')
print(schools)

# We can clear the whole of a list using the ".clear()" function.
schools.clear()
print(schools)

#We can use the '.pop()' to remove a single value.

list2.pop(4)
print(list2)

#We can also use the 'del()' in replacement of ".pop()".
del list2[0]
print(list2)