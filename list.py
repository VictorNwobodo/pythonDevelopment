# Working with list in python.

countries = ['UK', 'US', 'USA', 'NG', 'Canada', 'China']
print(countries)

# Printing out a specific countries among the lists.
print(countries[4])

# Let get the second index of a country together with the country all together.
print(countries[5][2])
# this will look for the 5th index among the listed countries and get the second value of that country which in this case is "china" with the second index "i" will be printed.

# Finding what type of class a variable is.
print(type(countries))
print(type(countries[3]))

# Let say if we want to get the first index from our list.
print(countries[1:4])
print(countries[0:3])
print(countries[3:])
print(countries[3:5])

# changing a list name to another name.
countries[4] = 'Austrial'
print(countries)

# Two ways of getting a list value.

# Using the index number.
print(countries[3])

# Using a negative sign.
print(countries[-5])
#Note that the negative sign gets the value from the back or bottom.

#getting the length of a list.
print(len(countries))

#Second method of creating a list known as "list constructor"
states = list(('Enugu', 'Abia', 'Abuja', 'Lagos', 'Abia', 'Anambra', 'Imo', 'Ebonyi', 'Platue'))
print(states)
print(type(states))