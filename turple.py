# Turples are just the lists.
# Turples are immutable which simply means that it cannot be replace.

staff = ('Sandra', 'Michael', 'Samuel', 'Stacy')
print(staff[3])

# Lets try to reassign a variable and see what will happen.
# lists = ('garri', 'fruits', 'groccerries')
# lists[2] = 'toiletries'
# print(lists)

# Turple allows the repetition of same values which will work just fine.
numbers = (1,3,4,4,23,2,1,1,1,1,1)
print(max(numbers))
print(type(numbers))
print(min(numbers))
print(numbers)

# Allows various datatype.

boo = (True, False, True)
print(boo)

strings = ('Home', 'Market', 'Crpto')
print(strings)

# Turples also accepting combinations of different datatypes.
mixed = ('hello', True, 23, False, 34.5, 'State', 30 + 34)
print(mixed)

