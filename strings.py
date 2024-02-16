print("Hello \nVictor")
# We can get a single value from our string variable or integer using the "[]" function method.

name = "Victor"
print(name[5])
# Note that this can be applicable to range of numbers.

# We can also convert the variable to an uppercase letter if we want to.

university = "University of Nigeria Enugu State"
state = "ENUGU STATE NIGERIA"
print(university.upper())
#notice we have "upper()" and not "uppercase()", why because python doe not understand the syntax like javascript does so we then use the "upper()" function in convertion of strings. The same is applicable to "lower()".

#checking if a variable is in "uppercase" or in "lowercase".
print(state.isupper())
#so it checks and parse a boolean statement of True or False.

#We can also join two function together like converting from one case to another and same time checking if that same value is the opposite. for example:

print(university.upper().islower())


# but when we say isupper() we are going to get the value True.
print(university.upper().isupper())

#getting the "length" of a string or integer we use the function "len(the variable)"

print(len(state))